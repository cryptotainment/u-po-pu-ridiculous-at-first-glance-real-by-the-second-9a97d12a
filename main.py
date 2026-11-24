#!/usr/bin/env python3
"""make.fun entry: Ridiculous at First Glance, Real by the Second.

Writes one sentence (<=200 chars) pitching a bizarre startup idea that
sounds absurd until you see the business logic, to /output/entry.txt.
Python 3.13 standard library only. Deterministic: same bytes every run.
"""

import hashlib
import os
import sys

LINE = (
    "We sell naming rights to potholes: a mattress brand sponsors the crater, "
    "the city finally patches it, and drivers stop losing hubcaps to a hole "
    "with a logo on it."
)


def main() -> int:
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        print(f"gate failed: length {len(text)} not in 1..200", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate failed: blank text", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("gate failed: not a single line", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = text.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    print(f"wrote {path}: {len(text)} chars, sha256 "
          f"{hashlib.sha256(data).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
