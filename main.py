#!/usr/bin/env python3
"""The Perfect Pickup Line -- make.fun entry (program/v1).

Writes one short pickup line (a single line of at most 200 characters)
to entry.txt in MAKEFUN_OUTPUT_DIR (or /output when unset), then reads it
back and verifies it byte-for-byte. Standard library only.
"""

import os
import sys

TEXT = (
    "That laugh of yours just cost me the 7:42 \u2014 best missed train "
    "of my life, and I'll be on this platform again tomorrow at eight."
)


def main() -> int:
    # Gate: non-empty, a single line, at most 200 characters.
    if not TEXT or not TEXT.strip():
        print("gate failed: entry is empty", file=sys.stderr)
        return 1
    if len(TEXT) > 200:
        print(
            "gate failed: entry is %d characters (> 200)" % len(TEXT),
            file=sys.stderr,
        )
        return 1
    if "\n" in TEXT or "\r" in TEXT:
        print("gate failed: entry contains a newline", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    # Read back and verify byte-for-byte.
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != TEXT:
        print(
            "gate failed: entry.txt does not match TEXT byte-for-byte",
            file=sys.stderr,
        )
        return 1

    print("wrote %s (%d characters)" % (path, len(TEXT)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
