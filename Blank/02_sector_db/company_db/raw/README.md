# Raw Source Files

This folder stores downloaded evidence files for the company DB.

These files are not final test fixtures. They are raw source material used to populate audited JSON fixtures in `07_implementation/data/raw/`.

## Subfolders

| Folder | Content |
|---|---|
| `sec/` | SEC JSON downloaded from `data.sec.gov` |
| `ir/MSFT/` | Microsoft investor relations raw pages |
| `ir/AMZN/` | Amazon investor relations / About Amazon raw pages |
| `ir/PTT/` | PTT investor relations and SET raw pages |

## Rules

1. Keep raw files unedited.
2. Store cleaned/extracted versions in `../processed/`.
3. Store final fixture JSON in `07_implementation/data/raw/`.
4. If a downloaded file is a shell/redirect page, mark it in `../download_log.md` before using it.
