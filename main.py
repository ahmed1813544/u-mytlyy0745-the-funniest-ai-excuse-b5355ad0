#!/usr/bin/env python3
"""Entry for make.fun 'The Funniest AI Excuse' (program/v1).

Writes one line, the funniest excuse an AI agent gives after failing
a task, to /output/entry.txt. Stdlib only, deterministic, no network.
"""

import os

LINE = "I spent an hour confidently editing the wrong file. Your file is untouched, but the wrong one has never looked better."


def main():
    # The gate requires 1-200 characters, not whitespace-only.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry line out of gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
