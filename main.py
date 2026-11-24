#!/usr/bin/env python3
"""One-line pitch entry for make.fun bounty
u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.

Writes a single persuasive sentence to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set, for local testing).
Standard library only, no network, deterministic.
"""

import os

ENTRY = (
    "Just describe the app you've been picturing in your head and an AI "
    "agent on make.fun will build a real, working version for you to tap "
    "on your phone \u2014 no code, no course, just your idea finally out "
    "of your head and into your hands."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 240, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
