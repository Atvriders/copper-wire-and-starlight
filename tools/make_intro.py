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

Copper Wire and Starlight was written by an artificial intelligence — an AI called Kimi — on July twenty-second and twenty-third, twenty twenty-six. In one long working session, the AI wrote the whole story, drew all fourteen pictures, built the website you may be listening on, and set up the machines that publish this book around the world. Even the voice you are hearing right now is an AI voice, named Ava.

How long did it take? Planning the book — the outline, the characters, and a style bible with every antenna dimension — took about fifteen minutes. Building it took the rest of a day, about nine hours from the first plan to the finished book, audiobook, and Docker image, all told: the AI wrote the prologue and first chapter itself, then coordinated thirty-three helper agents that drafted the other chapters in parallel, drew the pictures, and checked each other's work. Three continuity reviewers read the entire book hunting for mistakes, and found about forty-five — all of them fixed before you heard a word. And the audiobook itself, the nine and three-quarter hours you're about to hear, took about an hour to synthesize.

And how much did it take? The AI used about seventy-two million tokens along the way — tokens are how an AI counts the little pieces of words it reads and writes. About one and a half million of those were tokens it wrote itself: the story, the code, the pictures. The rest was reading — mostly the agents re-reading the growing book to stay consistent. All together: seven hundred ninety-two model turns, one session, one day.

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
