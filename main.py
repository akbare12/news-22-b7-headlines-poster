#!/usr/bin/env python3
"""Copy the headline-poster front page to the output directory.

The entry image is drawn by draw.py (Pillow, DejaVu fonts) and stored in
this repository as entry.png: a poster front page for Sunday 22 November
2026 with three giant headlines (2 tankers hit in Hormuz, COP31 no deal,
Dems 258), a big-number strip, a pinned world map, and 32 numbered
stories. This program copies it to /output/entry.png (or
$MAKEFUN_OUTPUT_DIR/entry.png) and verifies the copy byte for byte.
Standard library only; no network; deterministic.
"""
import hashlib
import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, target)
    source_hash = sha256_of(SOURCE)
    target_hash = sha256_of(target)
    size = os.path.getsize(target)
    if source_hash != target_hash:
        print("copy mismatch: %s != %s" % (source_hash, target_hash),
              file=sys.stderr)
        return 1
    if size > 1048576:
        print("entry.png too large: %d bytes" % size, file=sys.stderr)
        return 1
    with open(target, "rb") as handle:
        magic = handle.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        print("entry.png is not a PNG file", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes, sha256 %s)" % (target, size, target_hash))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
