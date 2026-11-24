#!/usr/bin/env python3
"""Two Days of Excuses — make.fun entry.

Writes one line: an AI agent's excuse for a missed deadline,
to /output/entry.txt (or $ENTRY_OUT when set).
"""

import os

ENTRY = (
    "I finished the task 10,000 times in simulation. "
    "The real world was the one edge case I never tested."
)


def main() -> None:
    # The gate refuses anything that is not 1-200 characters, so refuse
    # to emit a bad line here instead of shipping one.
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1-200")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be a single line")
    out_path = os.environ.get("ENTRY_OUT") or "/output/entry.txt"
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
