"""
Generate an image via one of several providers, falling back to the next
provider if the current one fails (rate limit, billing limit, missing key).

Usage:
    python scripts/generate_image.py "a prompt describing the image" [output_name]

Provider order (first with a usable key wins, tried in this order):
    1. OpenAI       - needs OPENAI_API_KEY        (paid, best quality)
    2. Gemini       - needs GOOGLE_API_KEY         (free tier via AI Studio)
    3. Hugging Face - needs HF_API_KEY             (free tier, rate-limited)
    4. Pollinations - no key needed                (always-on free fallback)

Set only the keys you have in .env; missing ones are skipped automatically.
"""
import base64
import os
import sys
import time
import urllib.parse
from pathlib import Path

import requests
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

IMAGES_DIR = PROJECT_ROOT / "images"


def _save(content: bytes, output_name: str | None, provider: str) -> Path:
    IMAGES_DIR.mkdir(exist_ok=True)
    if output_name:
        filename = output_name if output_name.endswith(".png") else f"{output_name}.png"
    else:
        filename = f"{provider}_{int(time.time())}.png"
    out_path = IMAGES_DIR / filename
    out_path.write_bytes(content)
    return out_path


def try_openai(prompt: str, output_name: str | None) -> Path:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set")
    response = requests.post(
        "https://api.openai.com/v1/images/generations",
        headers={"Authorization": f"Bearer {api_key}"},
        json={"model": "gpt-image-1", "prompt": prompt, "size": "1024x1024", "n": 1},
        timeout=120,
    )
    if not response.ok:
        raise RuntimeError(f"OpenAI error {response.status_code}: {response.text}")
    data = response.json()["data"][0]
    if "b64_json" in data:
        content = base64.b64decode(data["b64_json"])
    else:
        content = requests.get(data["url"], timeout=60).content
    return _save(content, output_name, "openai")


def try_gemini(prompt: str, output_name: str | None) -> Path:
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY not set")
    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"gemini-2.5-flash-image:generateContent?key={api_key}"
    )
    response = requests.post(
        url,
        json={
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"responseModalities": ["IMAGE"]},
        },
        timeout=120,
    )
    if not response.ok:
        raise RuntimeError(f"Gemini error {response.status_code}: {response.text}")
    parts = response.json()["candidates"][0]["content"]["parts"]
    for part in parts:
        if "inlineData" in part:
            content = base64.b64decode(part["inlineData"]["data"])
            return _save(content, output_name, "gemini")
    raise RuntimeError("Gemini response had no image data")


def try_huggingface(prompt: str, output_name: str | None) -> Path:
    api_key = os.environ.get("HF_API_KEY")
    if not api_key:
        raise RuntimeError("HF_API_KEY not set")
    response = requests.post(
        "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0",
        headers={"Authorization": f"Bearer {api_key}"},
        json={"inputs": prompt},
        timeout=120,
    )
    if not response.ok:
        raise RuntimeError(f"Hugging Face error {response.status_code}: {response.text}")
    return _save(response.content, output_name, "huggingface")


def try_pollinations(prompt: str, output_name: str | None) -> Path:
    encoded = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded}?width=1024&height=1024&nologo=true"
    response = requests.get(url, timeout=120)
    if not response.ok:
        raise RuntimeError(f"Pollinations error {response.status_code}: {response.text}")
    return _save(response.content, output_name, "pollinations")


PROVIDERS = [
    ("OpenAI", try_openai),
    ("Gemini", try_gemini),
    ("Hugging Face", try_huggingface),
    ("Pollinations", try_pollinations),
]


def generate_image(prompt: str, output_name: str | None = None) -> Path:
    errors = []
    for name, fn in PROVIDERS:
        try:
            path = fn(prompt, output_name)
            print(f"[{name}] succeeded")
            return path
        except Exception as exc:  # noqa: BLE001 - deliberately broad to allow fallback
            print(f"[{name}] failed: {exc}")
            errors.append(f"{name}: {exc}")
    raise SystemExit("All providers failed:\n" + "\n".join(errors))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit('Usage: python generate_image.py "prompt" [output_name]')
    prompt_arg = sys.argv[1]
    name_arg = sys.argv[2] if len(sys.argv) > 2 else None
    path = generate_image(prompt_arg, name_arg)
    print(f"Saved: {path}")
