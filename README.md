# Copper Wire and Starlight

*A ham radio story for young builders — a novel for high-school readers about the
joy of building antennas out of junk.*

Westridge High's Amateur Radio Club has two members, a storeroom it's about to
lose, and one year to prove it deserves to exist. Then June Alvarez pulls a dead
Kenwood TS-520S out of a dumpster. What follows is a year of antennas built from
trash — a pop-can dipole, an extension cord promoted to the sky, a broken tape
measure that hunts hidden transmitters, a Slinky in an attic, a copper J-pole
before the storm — and the particular joy of hearing a voice come back out of the
air on something you built with your own hands. Every antenna in the book is real,
every dimension is correct, and the recipes are in the back.

Written for high-school readers: the physics is real, the procedure is real, and
nobody talks down to anybody.

## How it was made

Written by **Kimi** (model `kimi-code/k3`) running in Kimi Code CLI on
**22–23 July 2026**, in a single long session that also produced the typeset
editions, the audiobook, the figures, this GitHub repo, and the Docker/CI
pipeline. Sibling projects:
**[200 Meters and Down](https://github.com/Atvriders/200-meters-and-down)** and
**[Mia and the Sky-Skipping Radio](https://github.com/Atvriders/ham-radio-storybook)**,
whose build machinery this repo reuses.

| | |
|---|---|
| **Sections** | Making-of introduction + prologue + 12 chapters + epilogue, plus 2 appendices |
| **Words** | ≈ 90,600 |
| **Illustrations** | 14 (hand-authored SVG, inlined at build time) |
| **Audiobook** | 17 tracks, ≈ 9¾ hours total (edge-tts, voice `en-US-AvaNeural`, −8%) |
| **Process** | A series bible ([`STYLE.md`](STYLE.md)), then 14 parallel writer agents, 3 continuity reviewers (≈ 45 fixes applied), 14 figure agents, and a tooling agent — all coordinated by the main agent, which wrote the Prologue and Chapter 1 itself |
| **Model turns** | 792 across 34 agents (1 main + 33 subagents) |
| **Output tokens** | ≈ 1,549,000 — everything the model wrote: story, code, figures |
| **Total API tokens** | ≈ 71.9 million, summed over all turns (the agents re-read the growing book every turn; nearly all input was served from cache) |
| **Wall time** | ≈ 9 hours from first prompt to published image: ≈ 15 min planning, the writing/figure/tooling work mostly parallelized over the afternoon, and ≈ 1 hour of edge-tts synthesis for the 9¾-hour audiobook |

Measured at ship from the session's wire-log `usage` records.

## Formats

The sources are [`chapters/`](chapters/) and [`appendices/`](appendices/) (Markdown).
The typeset editions are built from them by CI into `build/` (not stored in git):

| File | What it is |
|---|---|
| `build/index.html` | The book as a single self-contained page — linked table of contents, all 14 illustrations inline. The nicest way to read it. |
| `build/copper-wire-and-starlight.pdf` | PDF edition (≈ 260 pages, one section per page break). |
| `build/copper-wire-and-starlight.txt` | Plain-text edition. |
| Audiobook ([release v1.0](https://github.com/Atvriders/copper-wire-and-starlight/releases/tag/v1.0)) | Spoken intro plus one MP3 per section (`intro.mp3`, `ch00.mp3` … `ch12.mp3`, `epilogue.mp3`, `appendix-a.mp3`, `appendix-b.mp3`), narrated with [edge-tts](https://pypi.org/project/edge-tts/) (voice `en-US-AvaNeural`) via [`tools/make_audiobook.py`](tools/make_audiobook.py) and [`tools/make_intro.py`](tools/make_intro.py). **≈ 9 hours 45 minutes total.** Not stored in git. |
| [`figures/`](figures/) | The 14 illustrations as hand-authored SVG, inlined into the HTML/PDF editions at build time. |
| [`STYLE.md`](STYLE.md) | The series bible: cast, timeline, call signs, the technical canon table (every antenna dimension in the book), style laws, and per-chapter beats. |
| [`Dockerfile`](Dockerfile) / [`docker-compose.yml`](docker-compose.yml) | Serve the book yourself — see below. |

## Docker

The image packages the book and the audiobook behind nginx, built and pushed to
`ghcr.io/atvriders/copper-wire-and-starlight` by CI on every push to `main`.
On any Docker host:

```sh
docker compose pull && docker compose up -d
```

Serves the book at [http://localhost:3025](http://localhost:3025) and the
audiobook player at `/audiobook/`.

To build locally instead: regenerate the typeset editions, fetch the audiobook
from the release (it is not stored in git), then build the image:

```sh
pip install -r requirements.txt
python3 tools/build_book.py --html --txt --pdf --out build/
# fetch audiobook/ from release v1.0 (see .github/workflows/build.yml), then:
docker build -t ghcr.io/atvriders/copper-wire-and-starlight:latest .
```
