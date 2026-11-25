#!/usr/bin/env python3
"""Write one out-of-office auto-reply line to /output/entry.txt.

Funniest One-Line Out-of-Office Reply (make.fun, $2): the program writes
a single line of text, and a judge model picks the funniest one.
"""

import os

LINE = "I'm away until Monday — if it's urgent, it can wait, that's why I'm away."


def main():
    # Gate: entry.txt must be UTF-8 text of 1-160 characters, not only
    # white space.
    if not 1 <= len(LINE) <= 160 or not LINE.strip():
        raise ValueError("entry line must be 1-160 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
