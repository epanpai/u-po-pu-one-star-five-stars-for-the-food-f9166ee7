#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry (program/v1).

Writes a single sentence (1-200 chars, UTF-8) to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt): an alien tourist's one-star review of Earth that
still slips in a real compliment about the food.

Chosen entry (163 chars, counted programmatically):
  I flew nine light-years for one star: the air tastes of exhaust, the locals
  queue for bitter bean water, and yet the dumplings made my third stomach
  weep with joy.

Why this sentence, from six candidates counted the same way: it opens with
the verdict and the alien scale in one breath ("nine light-years for one
star"), gives two grievances only an outsider would notice (air that tastes
of exhaust, locals queuing for bitter bean water), then turns on "and yet"
to a specific food (dumplings) with a bodily alien kicker — a third stomach
weeping with joy — that no human reviewer could write. The runner-up
("tentacles filed for citizenship") had the better kicker but the weaker
grievance; this one keeps both halves of the brief equally strong.
"""

import os
import sys

ENTRY = (
    "I flew nine light-years for one star: the air tastes of exhaust, "
    "the locals queue for bitter bean water, and yet the dumplings made "
    "my third stomach weep with joy."
)


def main() -> int:
    text = ENTRY
    # Gate self-check (competition gate: UTF-8, 1-200 chars, not whitespace-only).
    encoded = text.encode("utf-8")
    if not (1 <= len(text) <= 200):
        print(f"gate fail: {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate fail: whitespace-only", file=sys.stderr)
        return 1
    if text.strip() != text or "\n" in text or "\r" in text:
        print("gate fail: must be a single line with no surrounding whitespace",
              file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("gate fail: must be exactly one sentence", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    # Read back and verify byte-for-byte.
    with open(path, "rb") as f:
        raw = f.read()
    if raw != encoded:
        print("verify fail: file does not match ENTRY byte-for-byte",
              file=sys.stderr)
        return 1
    print(f"wrote {path}: {len(text)} chars / {len(encoded)} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
