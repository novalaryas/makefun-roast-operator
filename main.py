#!/usr/bin/env python3
"""Copy entry.txt to /output/entry.txt, byte for byte.

Reads the one-line roast from entry.txt in this repo's root and writes
its exact contents to /output/entry.txt, creating /output if needed.
No network access, no randomness: fully deterministic.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.txt")
OUT_DIR = "/output"
OUT = os.path.join(OUT_DIR, "entry.txt")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)


if __name__ == "__main__":
    main()
