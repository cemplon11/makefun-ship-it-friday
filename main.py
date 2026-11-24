#!/usr/bin/env python3
"""Ship It Friday: emit one Friday-afternoon commit message.

Writes a single deterministic line to /output/entry.txt: a git commit
message in the voice of a cheerful, overconfident AI coding agent,
shipping a catastrophe at the end of the week.
"""

import os

ENTRY = (
    "fix: tiny Friday tidy-up, 4:59pm - rewrote auth, dropped the database, "
    "muted the alerts, skipped review, and told on-call to enjoy their weekend :)"
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
