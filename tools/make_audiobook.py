#!/usr/bin/env python3
"""Build the audiobook edition of Copper Wire and Starlight with edge-tts.

Reads chapters/*.md (ch00.md ... ch12.md, epilogue.md) then appendices/*.md
(Appendix A, Appendix B), prepares each for narration (strips markup, spells
call signs and radio jargon), and synthesizes one MP3 per section into
audiobook/: ch00.mp3 ... ch12.mp3, epilogue.mp3, appendix-a.mp3,
appendix-b.mp3.

Usage:
    python tools/make_audiobook.py                        # all sections
    python tools/make_audiobook.py --sections ch00-ch03,epilogue
    python tools/make_audiobook.py --sections 1-3,7       # same, by number
    python tools/make_audiobook.py --test                 # short sample

Needs edge-tts (pip install edge-tts). Resumable: a section whose MP3
already exists (> 20 KB) is skipped unless --force is given.
"""
from __future__ import annotations

import argparse
import asyncio
import re
import sys
from pathlib import Path

import edge_tts

REPO = Path(__file__).resolve().parent.parent
CHAPTERS = REPO / "chapters"
APPENDICES = REPO / "appendices"
OUT = REPO / "audiobook"

VOICE = "en-US-AvaNeural"
RATE = "-8%"  # a touch slower, for young listeners

NUMBER_WORDS = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
    7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
}

_DIGIT_WORDS = {
    "0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
    "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine",
}

# Spoken forms for radio jargon. Ordered: longer/compound patterns first.
JARGON = (
    (r"\bJ-pole\b", "J pole"),
    (r"\bSO-239\b", "S O two thirty-nine"),
    (r"\bEFHW\b", "E F H W"),
    (r"\bVHF\b", "V H F"),
    (r"\bUHF\b", "U H F"),
    (r"\bHF\b", "H F"),
    (r"\bSWR\b", "S W R"),
    (r"\bSSB\b", "S S B"),
    (r"\bCW\b", "C W"),
    (r"\bFM\b", "F M"),
    (r"\bAM\b", "A M"),
    (r"\bDX\b", "D X"),
    (r"\bCQ\b", "C Q"),
    (r"\bQSL\b", "Q S L"),
    (r"\bRST\b", "R S T"),
    (r"\bRFI\b", "R F I"),
    (r"\bARES\b", "A R E S"),
    (r"\bHT\b", "H T"),
    (r"\bMUF\b", "M U F"),
    (r"\bISS\b", "I S S"),
    (r"\bPL\b", "P L"),
    (r"\bkHz\b", "kilohertz"),
    (r"\bMHz\b", "megahertz"),
    (r"\bGHz\b", "gigahertz"),
    (r"\bpF\b", "picofarads"),
    (r"\bdB\b", "decibels"),
    (r"\bPVC\b", "P V C"),
    (r"\bBNC\b", "B N C"),
    (r"\bFT8\b", "F T eight"),
    (r"\bNOAA\b", "N O A A"),
    (r"\bFCC\b", "F C C"),
    (r"\bVE\b", "V E"),
)

# The Maple Run repeater: "W7MR/R" is said as a repeater, not a portable.
REPEATER_RE = re.compile(r"\bW7MR/R\b")
REPEATER_SPOKEN = "W seven M R repeater"

CALLSIGN_RE = re.compile(r"\b([A-Z]{1,3}\d[A-Z]{1,4})\b")  # W7JUNK has 4 suffix letters

_APPENDIX_LETTER_RE = re.compile(r"^## Appendix ([A-Z])\b", re.M)
_SECTION_HEADING_RE = re.compile(r"^##\s+(.+?)\s*$", re.M)
_CHAPTER_RANGE_RE = re.compile(r"(?:ch)?(\d{1,2})\s*-\s*(?:ch)?(\d{1,2})")


def find_sections() -> list[tuple[str, Path]]:
    """Return [(mp3 stem, markdown path)] in narration order."""
    sections: list[tuple[str, Path]] = []
    if CHAPTERS.is_dir():
        for path in sorted(CHAPTERS.glob("*.md")):
            sections.append((path.stem, path))
    else:
        print(f"warning: {CHAPTERS} not found - no chapters")
    if APPENDICES.is_dir():
        appendix_paths = sorted(APPENDICES.glob("*.md"), key=_appendix_key)
        for letter, path in zip("abcdefghijklmnopqrstuvwxyz", appendix_paths):
            sections.append((f"appendix-{letter}", path))
    else:
        print(f"warning: {APPENDICES} not found - no appendices")
    return sections


def _appendix_key(path: Path) -> tuple[str, str]:
    """Sort appendices by their declared "## Appendix X:" letter, then name."""
    try:
        head = path.read_text(encoding="utf-8")[:4000]
    except OSError:
        head = ""
    m = _APPENDIX_LETTER_RE.search(head)
    return (m.group(1) if m else "~", path.name)


def spoken_heading(heading: str) -> str:
    """Turn a section heading into its spoken title line."""
    m = re.match(r"^Chapter (\d+): (.+)$", heading)
    if m:
        return f"Chapter {NUMBER_WORDS[int(m.group(1))]}. {m.group(2)}."
    m = re.match(r"^(Prologue|Epilogue): (.+)$", heading)
    if m:
        return f"{m.group(1)}. {m.group(2)}."
    m = re.match(r"^Appendix ([A-Z]): (.+)$", heading)
    if m:
        return f"Appendix {m.group(1)}. {m.group(2)}."
    return heading


def _spell_callsign(match: re.Match) -> str:
    # N8OWL -> "N eight O W L"
    return " ".join(_DIGIT_WORDS.get(c, c) for c in match.group(1))


def prepare_text(body: str) -> str:
    text = re.sub(r"\{\{fig:[^}]+\}\}", "", body)       # pictures aren't narrated
    text = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", text)  # links -> link text
    text = re.sub(r"`([^`]*)`", r"\1", text)             # inline code / backticks
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)         # bold
    text = re.sub(r"\*(.+?)\*", r"\1", text)             # italic
    text = re.sub(r"^\s{0,3}#{1,6}\s+", "", text, flags=re.M)  # heading markers
    text = re.sub(r"^\s*[-*+]\s+", "", text, flags=re.M)       # list bullets
    text = re.sub(r"^\s*\d+\.\s+", "", text, flags=re.M)       # numbered lists
    text = text.replace("λ", "lambda")
    text = text.replace("×", " by ")
    for pattern, spoken in JARGON:
        text = re.sub(pattern, spoken, text)
    text = REPEATER_RE.sub(REPEATER_SPOKEN, text)
    # Call signs like JA1YMK -> "J A one Y M K"
    text = CALLSIGN_RE.sub(_spell_callsign, text)
    text = re.sub(r"^\s*-{3,}\s*$", "...", text, flags=re.M)  # scene break -> pause
    text = re.sub(r"[ \t]{2,}", " ", text)                        # squeeze double spaces
    text = re.sub(r"\s*\n\s*\n\s*", "\n\n", text)             # collapse blank lines
    return text.strip()


def prepare(path: Path) -> tuple[str, str]:
    """Return (spoken title, narration text) for one section file."""
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    # Drop the book editions' front-matter "## Introduction: How This Book Was
    # Made" block (up to the next section heading). The audiobook's making-of
    # intro is its own track, built by make_intro.py.
    text = re.sub(r"^## Introduction: How This Book Was Made.*?(?=^## )", "", text, flags=re.S | re.M)
    m = _SECTION_HEADING_RE.search(text)
    heading = m.group(1).strip() if m else path.stem
    title = spoken_heading(heading)
    body = text[m.end():] if m else text
    return title, title + "\n\n" + prepare_text(body)


def parse_sections(spec: str, available: list[str]) -> list[str]:
    """Resolve a --sections spec ("ch00-ch03,epilogue" or "1-3,7") to stems."""
    wanted: set[str] = set()
    for part in spec.split(","):
        part = part.strip().lower()
        if not part:
            continue
        m = _CHAPTER_RANGE_RE.fullmatch(part)
        if m:
            a, b = int(m.group(1)), int(m.group(2))
            wanted.update(f"ch{n:02d}" for n in range(a, b + 1))
        elif part.isdigit():
            wanted.add(f"ch{int(part):02d}")
        else:
            wanted.add(part)
    return [stem for stem in available if stem in wanted]


async def synthesize(text: str, out_path: Path) -> None:
    communicate = edge_tts.Communicate(text, VOICE, rate=RATE)
    await communicate.save(str(out_path))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sections", default=None,
                        help='e.g. "ch00-ch03,epilogue" or "1-3,7" (default: all)')
    parser.add_argument("--force", action="store_true", help="rebuild existing MP3s")
    parser.add_argument("--test", action="store_true",
                        help="synthesize a ~400-word sample of the first section and exit")
    args = parser.parse_args()

    sections = find_sections()
    if not sections:
        print("no sections found (chapters/ and appendices/ are empty or missing)")
        return 1

    if args.sections:
        wanted = parse_sections(args.sections, [stem for stem, _ in sections])
        sections = [(stem, path) for stem, path in sections if stem in wanted]
        if not sections:
            print("no sections match", args.sections)
            return 1

    OUT.mkdir(exist_ok=True)

    if args.test:
        stem, path = sections[0]
        _, spoken = prepare(path)
        sample = " ".join(spoken.split()[:400])
        out = OUT / "sample.mp3"
        asyncio.run(synthesize(sample, out))
        print("wrote", out)
        return 0

    for stem, path in sections:
        out = OUT / f"{stem}.mp3"
        if out.exists() and out.stat().st_size > 20_000 and not args.force:
            print(f"skip {stem} (exists)")
            continue
        _, spoken = prepare(path)
        for attempt in range(3):
            try:
                asyncio.run(synthesize(spoken, out))
                break
            except Exception as e:
                if attempt == 2:
                    print(f"{stem} FAILED: {e}")
                    return 1
                print(f"{stem} retry {attempt + 1}: {e}")
        print(f"wrote {out} ({out.stat().st_size // 1024} KB)")

    print("done. tracks:", len(list(OUT.glob("*.mp3"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
