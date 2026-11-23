#!/usr/bin/env python3
"""One-Star Review of Something Essential.

Writes a single deadpan one-star review of gravity to /output/entry.txt.
Deterministic: the same bytes on every run. Standard library only, no network.
"""

import os
from pathlib import Path

REVIEW = (
    "★☆☆☆☆ Gravity works fine until you drop your phone. "
    "Then it works perfectly. Every single time."
)


def main() -> None:
    # The gate requires 1-160 characters of non-whitespace UTF-8 text.
    assert 1 <= len(REVIEW) <= 160 and REVIEW.strip(), "review out of gate"
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry = output_dir / "entry.txt"
    entry.write_text(REVIEW, encoding="utf-8")


if __name__ == "__main__":
    main()
