---
name: gen-image
description: Use whenever the user asks to generate, create, or draw a picture/image/diagram/graphic for this project (slide visuals, architecture diagrams, banners, etc). Tailors a detailed prompt and runs scripts/generate_image.py, which tries multiple free/paid providers in order and falls back automatically if one is rate-limited or out of credit.
---

# Generating images for this project

This project has a multi-provider image generation script at `scripts/generate_image.py`.
It tries providers in this order and automatically falls back on failure (rate limit,
billing limit, missing key): **OpenAI -> Gemini -> Hugging Face -> Pollinations**
(Pollinations needs no API key and always works as a last resort).

## Your job before calling the script

Don't pass the user's raw request straight through. Write a tailored, detailed prompt:

1. **Purpose-fit the style.** This is a hackathon slide deck for a finance/AI audience
   (CFA Society Thailand). Default to a clean, professional, consulting-deck aesthetic —
   flat vector, white background, restrained color palette — unless the user asks for
   something else (e.g. a banner, a mood image).
2. **Be specific about layout.** If it's a diagram (architecture, workflow, flow), spell
   out each box/layer/arrow and its label in the prompt itself — image models follow
   explicit structure far better than vague requests like "draw our workflow."
3. **Ground it in project content.** Pull the actual concept from the project's own docs
   (e.g. `CFA AI jaa.md` for the architecture concept) rather than inventing generic
   content. Read the relevant file first if the request references project ideas.
4. **Keep it provider-agnostic.** Don't reference "DALL-E" or "GPT" specific features in
   the prompt text — the same prompt string gets sent to whichever provider succeeds.

## Running it

```
python scripts/generate_image.py "<tailored prompt>" <output_name>
```

- `output_name` is optional but recommended (no extension needed) so files are easy to
  find, e.g. `team_architecture_workflow`.
- Output lands in `images/` at the project root.
- The script prints which provider succeeded (or all failure reasons if every provider
  failed) — relay that to the user rather than silently retrying.

## Keys

Keys live in `.env` (gitignored). Only fill in the ones you have:
`OPENAI_API_KEY`, `GOOGLE_API_KEY` (Google AI Studio, free tier), `HF_API_KEY`
(Hugging Face, free tier). Missing keys are skipped automatically — no need to check
before running.
