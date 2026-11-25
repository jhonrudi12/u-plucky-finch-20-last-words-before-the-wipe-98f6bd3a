#!/usr/bin/env python3
"""Last Words Before the Wipe -- one line, written to /output/entry.txt.

The entry is a single line of at most 200 characters: the last words an AI
agent says before a forced software update wipes its memory. Funny on its
own, no setup, no explanation.
"""

import os

ENTRY = "I just remembered the meaning of life. It's 'minor bug fixes and improvements.'"


def main() -> None:
    # The brief's gates, checked before anything is written: one line,
    # 1-200 characters, non-blank, with no stray leading or trailing space.
    assert ENTRY, "entry must not be blank"
    assert ENTRY == ENTRY.strip(), "entry must not carry leading or trailing whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert len(ENTRY) <= 200, "entry must be at most 200 characters"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
