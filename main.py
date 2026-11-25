#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry.

Writes a single-sentence alien-tourist review of Earth (<=200 chars)
to $OUTPUT_DIR/entry.txt (default /output/entry.txt).

The sentence: a three-beat grievance (fined for glowing, rained on,
queued like cattle) that flips into a specific food compliment
(banh mi: crackling pork and pickled carrot) — and the punch is
stranger than the premise: the food has corrupted the reviewer, who
now files the invasion report itself as a restaurant review.
"""

import os
import sys

SENTENCE = (
    "One star: I crossed galaxies to be fined for glowing, "
    "rained on, and queued like cattle \u2014 but one b\u00e1nh m\u00ec, "
    "crackling pork and pickled carrot, has me filing my invasion "
    "report as a restaurant review."
)


def main() -> int:
    text = SENTENCE
    # Gate self-check, mirroring the sealed scorer:
    # UTF-8 text, 1..200 characters, not only whitespace, one sentence.
    if not (1 <= len(text) <= 200):
        print(f"gate fail: {len(text)} chars, must be 1..200", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate fail: only whitespace", file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("gate fail: must be exactly one sentence", file=sys.stderr)
        return 1
    if any(c in text for c in "!?") or "\n" in text:
        print("gate fail: extra sentence terminator or newline", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
