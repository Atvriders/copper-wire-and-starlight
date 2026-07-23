#!/usr/bin/env python3
"""Build the spoken introduction for the audiobook with edge-tts.

The intro tells listeners how this book was made (and by what) and why it
exists. Writes audiobook/intro.mp3, published as a release asset alongside
the chapter tracks.

Usage:
    python tools/make_intro.py            # writes audiobook/intro.mp3
    python tools/make_intro.py --force    # rebuild even if it exists
"""
from __future__ import annotations

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.make_audiobook import OUT, synthesize

INTRO = """
Hello! Before our story begins, here is something special about how this book was made.

Copper Wire and Starlight was written by an artificial intelligence — an AI called Kimi — on July twenty-second, twenty twenty-six. In one long working session, the AI wrote the whole story, drew the pictures, built the website you may be listening on, and set up the machines that publish this book around the world. Even the voice you are hearing right now is an AI voice, named Ava.

Why make a book like this? Because somewhere out there is a kid who has never felt the joy of building an antenna out of junk — out of soda cans, a broken tape measure, a salvaged extension cord — and hearing a voice come back out of the sky. This book is for them. It is a story about four teenagers, a curmudgeonly old engineer, and a school radio club that refuses to die. Every antenna they build is real. Every one of them works. And you can build every single one yourself — the recipes are in the back of the book.

Seventy-three — that means best wishes, in ham talk. And now, enjoy Copper Wire and Starlight.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    OUT.mkdir(exist_ok=True)
    out = OUT / "intro.mp3"
    if out.exists() and out.stat().st_size > 20_000 and not args.force:
        print("skip intro (exists)")
        return 0
    asyncio.run(synthesize(" ".join(INTRO.split()), out))
    print(f"wrote {out} ({out.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
