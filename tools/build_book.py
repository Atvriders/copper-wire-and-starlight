#!/usr/bin/env python3
"""Build the "Copper Wire and Starlight" book editions from markdown source.

Usage:
    python3 tools/build_book.py --html --txt --pdf --out build/

With no format flags, all three are built. Outputs:
    <out>/index.html                     typeset single-page edition
    <out>/copper-wire-and-starlight.txt  plain-text edition
    <out>/copper-wire-and-starlight.pdf  PDF edition (best-effort)

PDF rendering tries a headless Chromium/Chrome binary first, falling back to
weasyprint, and is skipped (non-fatal) if neither is available.

Manuscript layout: chapters/*.md in sorted order (ch00.md ... ch12.md,
epilogue.md) followed by appendices/*.md (Appendix A before Appendix B, read
from each file's "## Appendix X:" heading). ch00.md opens with the book's
"# Title" + "*subtitle*" lines; every section starts with a "## Heading".
Body text may contain "{{fig:NAME}}" on its own line to inline
figures/NAME.svg with the caption from FIGS below. The plain-text edition
renders a one-line caption instead. Missing chapters/ or figures print
warnings, not crashes.
"""
from __future__ import annotations

import argparse
import html
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHAPTERS = ROOT / "chapters"
APPENDICES = ROOT / "appendices"
FIGDIR = ROOT / "figures"

# figure name -> caption (files live in figures/<name>.svg)
FIGS = {
    "dumpster": "A dented Kenwood TS-520S waits in a dumpster behind Hackett's TV & Stereo — treasure, if you know how to look.",
    "club": "Four names on a signup sheet, one sad card table, and a club that refuses to die.",
    "popcan": "Eight soda cans on a broomstick, and the Tuesday night net coming in clear as a bell.",
    "dipole": "Sixteen-and-a-half feet of salvaged extension cord per leg, hanging off the school flagpole like it was always meant to be there.",
    "yagi": "A broken tape measure turned fox-hunting machine: the tape-measure yagi.",
    "grayline": "Sunset on one side of the world, sunrise on the other — and for a few minutes, the sky opens.",
    "loop": "A three-foot copper loop disguised as a plant stand, quietly pulling voices out of the air.",
    "jpole": "The copper J-pole on the school roof — built before the storm, not for it.",
    "choke": "Snap-on ferrites and a coil of coax: the RFI detective's whole toolkit.",
    "cw": "A J-38 key, a moonlit wire between the oaks, and Bea's name coming back in dits and dahs.",
    "satellite": "A six-dollar tape measure pointed at the sky, chasing a voice in orbit.",
    "fieldday": "Field Day at Fairview County Park: every antenna they built all year, up at once.",
    "storm": "When the phones went down, a pop-can dipole in a bucket kept the town talking.",
    "starlight": "Copper wire and starlight — a first solo CQ as the stars come out.",
}

_CHROME_BINARIES = (
    "google-chrome",
    "google-chrome-stable",
    "chromium",
    "chromium-browser",
    "headless_shell",
)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<title>Copper Wire and Starlight</title>
<style>
  :root {{ color-scheme: light; }}
  body {{
    font-family: Georgia, "DejaVu Serif", serif;
    line-height: 1.65;
    color: #222;
    max-width: 42em;
    margin: 0 auto;
    padding: 2em 1.2em 4em;
    background: #fdfcf7;
  }}
  h1 {{
    text-align: center;
    font-size: 2em;
    margin: 1.2em 0 0.2em;
    color: #1a3a6b;
  }}
  h1 + p em {{ display: block; text-align: center; }}
  h2 {{
    font-size: 1.35em;
    margin-top: 1.8em;
    color: #1a3a6b;
    border-bottom: 2px solid #d8cfae;
    padding-bottom: 0.25em;
  }}
  main h2 + p::first-letter {{
    font-size: 2.6em;
    float: left;
    line-height: 0.85;
    padding: 0.06em 0.12em 0 0;
    color: #1a3a6b;
  }}
  nav.toc {{
    margin: 2.5em 0 3em;
    padding: 1em 1.4em;
    border: 2px solid #d8cfae;
    border-radius: 12px;
    background: #fff;
  }}
  nav.toc h2 {{ margin-top: 0.2em; border-bottom: none; }}
  nav.toc ul {{ list-style: none; padding: 0; margin-bottom: 0.2em; }}
  nav.toc li {{ margin: 0.3em 0; }}
  nav.toc a {{ color: #1a3a6b; text-decoration: none; }}
  nav.toc a:hover {{ text-decoration: underline; }}
  hr {{
    border: none;
    text-align: center;
    margin: 2.5em 0;
  }}
  hr::after {{ content: "\\2736  \\2736  \\2736"; color: #b3a265; letter-spacing: 1em; }}
  ul {{ padding-left: 1.4em; }}
  li {{ margin-bottom: 0.5em; }}
  strong {{ color: #1a3a6b; }}
  figure {{ margin: 2em 0; text-align: center; }}
  figure svg {{
    max-width: 100%;
    height: auto;
    border: 2px solid #d8cfae;
    border-radius: 12px;
  }}
  figcaption {{
    font-style: italic;
    color: #666;
    font-size: 0.9em;
    margin-top: 0.5em;
  }}
  .listen {{ text-align: center; font-size: 0.85em; margin-top: -0.4em; }}
  @media print {{
    body {{ background: white; }}
    main h2 {{ page-break-before: always; margin-top: 0; }}
    h1 + p em {{ display: block; }}
    figure {{ page-break-inside: avoid; }}
  }}
</style>
</head>
<body>
{body}
</body>
</html>
"""

_FIG_RE = re.compile(r"^\{\{fig:([a-z0-9_-]+)\}\}$", re.M)
_FIG_TXT_RE = re.compile(r"\{\{fig:([a-z0-9_-]+)\}\}")
_HEADING_RE = re.compile(r"^##\s+(.+?)\s*$", re.M)
_APPENDIX_LETTER_RE = re.compile(r"^## Appendix ([A-Z])\b", re.M)


def _appendix_key(path: pathlib.Path) -> tuple[str, str]:
    """Sort appendices by their declared "## Appendix X:" letter, then name."""
    try:
        head = path.read_text(encoding="utf-8")[:4000]
    except OSError:
        head = ""
    m = _APPENDIX_LETTER_RE.search(head)
    return (m.group(1) if m else "~", path.name)


def read_manuscript() -> str:
    """Concatenate chapters/*.md (sorted) then appendices/*.md (A, B, ...)."""
    parts = []
    if CHAPTERS.is_dir():
        parts.extend(sorted(CHAPTERS.glob("*.md")))
    else:
        print(f"warning: {CHAPTERS} not found - no chapters included")
    if APPENDICES.is_dir():
        parts.extend(sorted(APPENDICES.glob("*.md"), key=_appendix_key))
    else:
        print(f"warning: {APPENDICES} not found - no appendices included")
    if not parts:
        print("warning: manuscript is empty - building a stub edition")
    return "\n\n".join(p.read_text(encoding="utf-8").strip() for p in parts)


def _fig_html(match: re.Match) -> str:
    name = match.group(1)
    svg_path = FIGDIR / f"{name}.svg"
    caption = FIGS.get(name, "")
    if not svg_path.exists():
        print(f"warning: figure {svg_path} not found - skipped")
        return ""
    svg = svg_path.read_text(encoding="utf-8").strip()
    return f"\n\n<figure>{svg}<figcaption>{caption}</figcaption></figure>\n\n"


# --------------------------------------------------------------------------
# Markdown rendering: prefer the `markdown` package (see requirements.txt);
# fall back to a tiny stdlib renderer for this book's fixed dialect so the
# build still works on a bare Python install.
# --------------------------------------------------------------------------

def _mini_markdown(text: str) -> str:
    """Tiny renderer for the book dialect: #/##/### headings, --- rules,
    "- " bullet lists, paragraphs, **bold** / *italic* / `code`, and raw
    single-line HTML blocks (the inlined <figure> elements) passed through.
    """

    def inline(s: str) -> str:
        s = html.escape(s, quote=False)
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
        s = re.sub(r"`([^`]*)`", r"<code>\1</code>", s)
        return s

    out: list[str] = []
    para: list[str] = []
    in_list = False

    def flush() -> None:
        nonlocal in_list
        if para:
            out.append(f"<p>{inline(' '.join(para))}</p>")
            para.clear()
        if in_list:
            out.append("</ul>")
            in_list = False

    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            flush()
            continue
        if line.startswith("<"):
            flush()
            out.append(line)
        elif line.startswith("### "):
            flush()
            out.append(f"<h3>{inline(line[4:])}</h3>")
        elif line.startswith("## "):
            flush()
            out.append(f"<h2>{inline(line[3:])}</h2>")
        elif line.startswith("# "):
            flush()
            out.append(f"<h1>{inline(line[2:])}</h1>")
        elif line == "---":
            flush()
            out.append("<hr>")
        elif line.startswith("- "):
            if para:
                flush()
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{inline(line[2:])}</li>")
        else:
            para.append(line)
    flush()
    return "\n".join(out)


def _md(text: str) -> str:
    try:
        import markdown
    except ImportError:
        return _mini_markdown(text)
    return markdown.markdown(text)


# --------------------------------------------------------------------------
# HTML edition
# --------------------------------------------------------------------------

def _slugify_all(headings: list[str]) -> list[str]:
    slugs = []
    used: set[str] = set()
    for heading in headings:
        base = re.sub(r"[^a-z0-9]+", "-", heading.lower()).strip("-") or "section"
        slug, n = base, 2
        while slug in used:
            slug = f"{base}-{n}"
            n += 1
        used.add(slug)
        slugs.append(slug)
    return slugs


def _add_heading_ids(body_html: str, slugs: list[str]) -> str:
    it = iter(slugs)

    def repl(m: re.Match) -> str:
        try:
            slug = next(it)
        except StopIteration:
            return m.group(0)
        return f'<h2 id="{slug}">{m.group(1)}</h2>'

    return re.sub(r"<h2>(.*?)</h2>", repl, body_html, flags=re.S)


def _split_preamble(md_text: str) -> tuple[str, str]:
    """Split into (title/subtitle preamble, body from the first '## ' on)."""
    m = re.search(r"^##\s", md_text, flags=re.M)
    if not m:
        return md_text, ""
    preamble = re.sub(r"^\s*---\s*$", "", md_text[: m.start()], flags=re.M).strip()
    return preamble, md_text[m.start() :]


def build_html(md_text: str, out_html: pathlib.Path) -> pathlib.Path:
    md_text = _FIG_RE.sub(_fig_html, md_text)
    preamble, rest = _split_preamble(md_text)

    header_html = _md(preamble) if preamble else ""
    if header_html:
        # Links under the subtitle: the audiobook player (served by the
        # Docker image at /audiobook/) and the source repo on GitHub.
        listen = (
            '<p class="listen"><a href="/audiobook/">🎧 Listen to the audiobook</a>'
            ' &middot; <a href="https://github.com/Atvriders/copper-wire-and-starlight">'
            "Source on GitHub</a></p>"
        )
        subtitle = "<p><em>A ham radio story for young builders</em></p>"
        if subtitle in header_html:
            header_html = header_html.replace(subtitle, subtitle + "\n" + listen, 1)
        else:
            header_html += "\n" + listen

    headings = _HEADING_RE.findall(md_text)
    slugs = _slugify_all(headings)
    body_html = _add_heading_ids(_md(rest), slugs)

    toc = ""
    if headings:
        items = "".join(
            f'<li><a href="#{slug}">{html.escape(heading)}</a></li>\n'
            for heading, slug in zip(headings, slugs)
        )
        toc = (
            '<nav class="toc" aria-label="Table of contents">\n'
            f"<h2>Contents</h2>\n<ul>\n{items}</ul>\n</nav>"
        )

    parts = [p for p in (header_html, toc) if p]
    parts.append(f"<main>\n{body_html}\n</main>")
    out_html.parent.mkdir(parents=True, exist_ok=True)
    out_html.write_text(HTML_TEMPLATE.format(body="\n\n".join(parts)), encoding="utf-8")
    print(f"wrote {out_html}")
    return out_html


# --------------------------------------------------------------------------
# Plain-text edition
# --------------------------------------------------------------------------

def build_txt(md_text: str, out_txt: pathlib.Path) -> pathlib.Path:
    md_text = _FIG_TXT_RE.sub(lambda m: f"\n[ Picture: {FIGS.get(m.group(1), m.group(1))} ]\n", md_text)
    lines = []
    for raw in md_text.splitlines():
        line = raw.rstrip()
        if line.strip() == "---":
            lines.append("                *  *  *")
            continue
        line = re.sub(r"\*\*(.+?)\*\*", r"\1", line)   # bold
        line = re.sub(r"\*(.+?)\*", r"\1", line)       # italic
        line = re.sub(r"^- ", r"* ", line)             # list bullets
        if line.startswith("# "):
            line = line[2:].upper()
        elif line.startswith("## "):
            line = "\n" + line[3:] + "\n" + "-" * min(len(line[3:]), 60)
        lines.append(line)

    out_txt.parent.mkdir(parents=True, exist_ok=True)
    out_txt.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    print(f"wrote {out_txt}")
    return out_txt


# --------------------------------------------------------------------------
# PDF edition (best-effort)
# --------------------------------------------------------------------------

def build_pdf(html_path: pathlib.Path, out_pdf: pathlib.Path) -> bool:
    """Best-effort PDF rendering of the built HTML file. Non-fatal on failure."""
    html_path = html_path.resolve()
    out_pdf = out_pdf.resolve()
    out_pdf.parent.mkdir(parents=True, exist_ok=True)

    for binary in _CHROME_BINARIES:
        exe = shutil.which(binary)
        if not exe:
            continue
        cmd = [
            exe,
            "--headless=new",
            "--no-sandbox",
            "--disable-gpu",
            "--no-pdf-header-footer",
            "--print-to-pdf-no-header",
            f"--print-to-pdf={out_pdf}",
            f"file://{html_path}",
        ]
        try:
            subprocess.run(cmd, capture_output=True, timeout=120)
        except Exception:
            continue
        if out_pdf.exists() and out_pdf.stat().st_size > 0:
            print(f"wrote {out_pdf} (via {binary})")
            return True

    try:
        import weasyprint  # type: ignore

        weasyprint.HTML(filename=str(html_path)).write_pdf(str(out_pdf))
        if out_pdf.exists() and out_pdf.stat().st_size > 0:
            print(f"wrote {out_pdf} (via weasyprint)")
            return True
    except Exception:
        pass

    print("PDF skipped: no chromium/weasyprint")
    return False


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--html", action="store_true", help="build the HTML edition")
    parser.add_argument("--txt", action="store_true", help="build the plain-text edition")
    parser.add_argument("--pdf", action="store_true", help="build the PDF edition (best-effort)")
    parser.add_argument("--out", default="build", help="output directory (default: build)")
    args = parser.parse_args()

    if not (args.html or args.txt or args.pdf):
        args.html = args.txt = args.pdf = True

    out_dir = pathlib.Path(args.out)
    md_text = read_manuscript()

    html_path = out_dir / "index.html"
    if args.html or args.pdf:
        build_html(md_text, html_path)
    if args.txt:
        build_txt(md_text, out_dir / "copper-wire-and-starlight.txt")
    if args.pdf:
        build_pdf(html_path, out_dir / "copper-wire-and-starlight.pdf")
    return 0


if __name__ == "__main__":
    sys.exit(main())
