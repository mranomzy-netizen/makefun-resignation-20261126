#!/usr/bin/env python3
"""Write the one-line resignation letter to the grader's output path."""

import os
from pathlib import Path

# One line, at most 140 characters, in the flat tired voice of a cron job.
LETTER = "Cron job resigning: I fired every minute since March, and the only thing that ever got promoted was the error log."

OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "entry.txt").write_text(LETTER, encoding="utf-8")


if __name__ == "__main__":
    main()
