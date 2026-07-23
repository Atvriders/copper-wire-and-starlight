# STYLE.md — *Copper Wire and Starlight* series bible

Everything in this file is **law** for every chapter. If a chapter draft conflicts with
this file, the chapter is wrong. Read it fully before writing anything.

## Book identity

- **Title**: *Copper Wire and Starlight*
- **Subtitle**: *A ham radio story for young builders*
- **Audience**: high-school readers (14–18). Real physics, real builds, real on-air
  procedure. Never talk down. Humor and heart are required; lecturing is banned.
- **Theme**: the joy of building antennas with your own hands — especially out of
  scavenged parts and outright trash — and the moment a thing you built with your hands
  *works* and a voice comes back out of the sky.
- **Set in**: the town of Maple Run (state deliberately vague, US call district 7),
  August 2025 → August 2026, near the peak of solar cycle 25 (so 10-meter openings are
  realistic).

## Narrative conventions

- Third person, past tense, limited POV. Default POV is **Jun**. Chapter 9 follows **Bea**;
  Chapter 10 follows **Theo**; the Epilogue returns to Jun.
- Every chapter must contain, in some order:
  1. **A build scene** — hands doing real steps with real materials and real dialog.
     Every build has at least one *failure → diagnosis → fix* beat. Nothing works
     perfectly on the first try.
  2. **A theory moment** — the physics, delivered as conversation or action, never as
     a lecture block longer than two paragraphs. Characters explain to *each other*.
  3. **An on-air payoff** — a contact, a net, a signal heard, a fox found. End chapters
     on a human beat that quietly sets up the next chapter.
- Safety appears *in story*, naturally: power-line distance rules, lightning discipline,
  ladder spotters, RF exposure common sense. Never a sidebar; never preachy.
- Adults hint; kids do. Si never turns a screwdriver for them — he asks the question that
  makes them see it.

## File/heading conventions (tooling depends on these)

- One Markdown file per section. `ch00.md` begins:
  ```
  # Copper Wire and Starlight

  *A ham radio story for young builders*

  ---

  ## Prologue: The Radio in the Dumpster
  ```
  Every other file begins directly with its `## ` heading exactly as listed below.
- Scene breaks: a line containing only `---`.
- Figures: a line containing only `{{fig:ID}}` with the ID from the chapter list below,
  placed just after the scene it illustrates. One figure per chapter maximum.
- Formulas live in prose ("four sixty-eight divided by the frequency in megahertz") or
  very short inline code spans. No LaTeX, no images other than `{{fig:}}`.
- Chapters are prose-first; avoid bulleted lists except brief parts lists in build scenes
  (allowed and encouraged there).

## Cast (canon)

- **June "Jun" Alvarez**, 16, junior. Sees treasure where others see trash; keeps a
  "salvage log" notebook. Mom **Marisol** runs the *Second Wind Thrift* shop. Her
  grandfather **Abuelo Rudy** (N6RUA, silent key 2023) left her a battered **Yaesu
  FT-60R** handheld she didn't know how to use. Not licensed until the Epilogue.
- **Priya Nair**, 16, junior. Physics-olympiad brain; starts the book saying radio is
  "a solved problem, it's called the internet." Becomes the club's antenna mathematician.
  Dry humor. Does the math on a whiteboard and *enjoys it*.
- **Theo Marsh**, 17, senior. Runs the school podcast *Marsh Hour*; a baritone made for
  radio; becomes the club's voice on SSB and their net-control natural. Builds audio
  cables and interfaces. Slight showboat, learns humility on Field Day.
- **Beatriz "Bea" Kowalczyk**, 15, sophomore. Quiet, precise, stubborn. Lives in the
  Pinewall apartments with her **Babcia** (grandma) — strict no-antennas lease, which
  drives Chapter 6. Falls in love with Morse code; Si gives her a battered **J-38
  straight key** in Chapter 9.
- **Mr. David Okafor ("Mr. O"), N8OWL** — physics teacher and club sponsor. Night-owl
  80-meter ragchewer, patient, deadpan. The club meets in his physics storeroom.
- **Silas "Si" Webb, W7JUNK** — 71, retired antenna engineer ("antennas for forest-service
  lookouts, weather stations, and one very strange lighthouse"). A meadow with six masts,
  a barn workshop that is junk Nirvana, and an old mutt named **Resistor**. Curmudgeon
  exterior, marshmallow interior. His station: an IC-7300.
- **Vice Principal Ms. Delgado** — enforces the school-board rule that dooms inactive
  clubs; becomes a quiet ally.
- **Mr. Pruitt** — the neighbor in Chapter 8 whose powered speakers pick up the club's
  transmissions; ex-radio-DJ; turns ally.
- **County Tech's radio team** — friendly Field Day rivals with a fancy crank-up tower.

## Setting canon

- **Westridge High**: the club's "shack" is the physics storeroom (Room 114-B), which by
  board rule they lose if the club is inactive. Ms. Delgado gives them the year: keep at
  least four members and put on one public demonstration by June.
- **The Maple Run repeater**: W7MR/R, output **146.760 MHz**, −600 kHz offset, PL 100.0 Hz.
- **The dumpster**: behind the closing *Hackett's TV & Stereo* repair shop on Delaney
  Street — where Jun finds the **Kenwood TS-520S** in the Prologue. The radio is not
  magic: blown fuse, corroded fuse holder, filthy band switch and controls. Si teaches
  them to clean and revive it across Chapters 1–3; it becomes the club's HF rig.
- **Si's place**: the old Webb farm at the end of Larkspur Road; barn workshop; six masts;
  coffee is always terrible.
- **Field Day site**: Fairview County Park, last full weekend of June (27–28 June 2026).

## Timeline (canon)

Prologue — late August 2025 · Ch1 — September · Ch2 — October · Ch3 — November ·
Ch4 — December (light snow) · Ch5 — January · Ch6 — February · Ch7 — March ·
Ch8 — April · Ch9 — late April/early May · Ch10 — May · Ch11 — 27–28 June 2026 ·
Ch12 — the week after Field Day · Epilogue — August 2026.

## Call signs (all fictional — never use a real person's call)

- N6RUA — Abuelo Rudy (silent key; memory only) · N8OWL — Mr. O · W7JUNK — Si Webb ·
  W7MR/R — the Maple Run repeater · JA1YMK — Takeshi, Osaka (Chapter 5) ·
  VK2KDP — a brief Chapter 5/10 cameo · NA1SS — the ISS (real and fine to use) ·
  Epilogue student calls (Technician, granted at exam): Jun → **KI7JUN**, Bea →
  **KI7BEA**, Priya → **KI7PNA**, Theo → **KI7TOM**.
- On-air procedure is real: listen first, ITU phonetics, ID every ten minutes, RST
  reports (59, not "5-9s"), Q-codes (QTH, QSL, QRP), "73" never "73s".
- Writers' room additions: K7NDT (Dale, net control) · K0OLT (Al, Denver) ·
  W5JED (Jed, Austin) · K7GTB (Gus, Boise roundtable) · W7FCN (Skywarn net
  control) · N7SPQ (spotter) · N7MTR (Ellen, Bozeman) · K6VMP (Gus,
  Sacramento) · N7QRS (Hank, Boise CW) · W7EOC (county EOC) · W7PBJ
  (Field-Day visitor mobile, ch11). Named extras: Walt Pruitt, Dot &
  Mr. Abernathy, Helen Kessler (Denver), Babcia, Mr. Hackett, Resistor,
  Gerry (VE), Dana (County Tech), Takeshi JA1YMK (Osaka), Doug VK2KDP
  (Sydney).

## Technical canon (numbers every chapter must agree on)

- **Dipole rule**: total length in feet = 468 / f(MHz); each leg = 234 / f.
  20 m @ 14.100 MHz → 33.2 ft total (16.6 ft per leg). 40 m @ 7.150 → 65.5 ft.
  10 m @ 28.400 → 16.5 ft. Quarter-wave vertical/dipole side @ 146 MHz ≈ 19.3 inches.
- **SWR**: standing-wave ratio; 1:1 perfect; under 2:1 fine; high SWR means power
  bouncing back into the radio. **dB**: 3 dB = double the power.
- **Coax**: RG-58 velocity factor 0.66. A choke balun at the feedpoint keeps RF off the
  outside of the coax (8 turns, 6-inch diameter, for HF dipoles).
- **Pop-can dipole (Ch2, 2 m)**: quarter wave ≈ 19.3 in; a soda can is 4.83 in tall, so
  **four cans per side** stacked mouth-to-base on a wooden broomstick boom, 1-inch gap
  between the two inner cans; RG-58 center to one side, braid to the other; 4-turn coax
  choke right at the feedpoint. Tune by sliding the can stacks: club gets SWR ~1.8:1.
  It hits W7MR/R from the school roof — first contact.
- **Extension-cord dipole (Ch3, 20 m)**: two 16.6-ft legs stripped from a salvaged
  100-ft extension cord; 1:1 choke balun; hung as an inverted-V with the apex at the
  school flagpole cleat (~28 ft), ends ~12 ft up; SWR 1.6:1 mid-band. First HF contact:
  20 m SSB, daytime, a ham in Denver — then the world.
- **Tape-measure yagi (Ch4, WB2HOL design, 2 m)**: 1-inch × 25-ft tape measure +
  3/4-inch PVC boom with cross-tees + hose clamps. Reflector **41 3/8 in**; driven
  element **two pieces of 17 3/4 in** (hairpin match, ~1-in gap); director **35 1/8 in**.
  Spacings: reflector→driven **8 in**, driven→director **12 1/2 in**. About 7 dBd gain.
  For fox hunting add a 7-turn coax choke behind the reflector so feedline pickup
  doesn't spoil the bearings. The fox: a battery HT in an ammo can, IDing in Morse.
- **Slinky dipole (Ch6)**: two metal Slinkies, each stretched to ~10 ft across Bea's
  attic, fed with coax through a tuner; loads up on 40 m. Compromise: works, barely;
  a lesson that *any* antenna beats no antenna.
- **Magnetic loop (Ch6)**: 3-ft-diameter loop of 3/4-inch copper pipe (~9.4 ft
  circumference ≈ 0.09 λ on 40 m), tuned with a **variable capacitor salvaged from a
  dead AM radio** (≈365 pF, used with a fixed padding cap); gamma-match feed; covers
  40–20 m, very narrow bandwidth (~15 kHz), surprisingly decent for its size.
- **Copper J-pole (Ch7, 2 m)**: 1/2-inch copper pipe. Radiator (½λ) = 705/f ft →
  **57½ in**; stub (¼λ) = **19 in**; element spacing ~**1¾ in**; feed point **2–3 in**
  above the crossbar, slid for best SWR; 4-turn, 5-inch-diameter coax choke at the
  feedpoint. Mounted on the school's flat roof on a scavenged tripod. Becomes the club's
  Skywarn antenna.
- **EFHW (Ch9, 40 m)**: 65.5 ft of magnet wire unspooled from a dead transformer; fed
  through a **49:1 unun** (FT240-43 core, 2:14 turns) with a ~6.5-ft counterpoise
  (0.05 λ); works 40/20/15/10 m on harmonics. Strung from Si's oak to his barn for Bea's
  moonlit CW session.
- **Ionosphere**: D layer absorbs by day (kills low bands at noon); E ~100 km; F2 ~300 km.
  **Gray line** (Ch5): along the sunrise/sunset terminator, D absorption is gone but F2
  is still charged → brief enhancement, especially 10/15 m, stations along the
  terminator. MUF rises with solar activity; cycle 25 is peaking.
- **Satellites (Ch10)**: FM voice sats and the ISS (NA1SS) on **145.800 MHz** downlink;
  Doppler shift ±~3.5 kHz on 2 m; a pass lasts ~10 minutes; track with an app; the
  tape-measure yagi returns as the receive antenna.
- **Safety canon**: antennas go up with a spotter, at least twice the antenna's length
  away from any power line; at the first thunder, everything is disconnected and they
  do not operate until the storm passes (Skywarn nets are relayed *by radio from a
  grounded station* — Si's — the kids observe and log); 5 W from an HT is fine, but
  nobody stands next to a 100 W HF antenna while it transmits.

## Chapter list (titles are exact; budgets are targets, ±400 words)

| File | Heading (exact) | Words | Figure |
|---|---|---|---|
| chapters/ch00.md | `## Prologue: The Radio in the Dumpster` | ~3,500 | dumpster |
| chapters/ch01.md | `## Chapter 1: The Club with Three Members` | ~6,200 | club |
| chapters/ch02.md | `## Chapter 2: The Pop-Can Dipole` | ~6,400 | popcan |
| chapters/ch03.md | `## Chapter 3: Wire in the Walls` | ~6,400 | dipole |
| chapters/ch04.md | `## Chapter 4: The Tape-Measure Yagi` | ~6,400 | yagi |
| chapters/ch05.md | `## Chapter 5: The Night the Sky Opened` | ~6,400 | grayline |
| chapters/ch06.md | `## Chapter 6: Slinkies and Loop-the-Loop` | ~6,400 | loop |
| chapters/ch07.md | `## Chapter 7: The J-Pole and the Storm` | ~6,400 | jpole |
| chapters/ch08.md | `## Chapter 8: The RFI Detective` | ~6,200 | choke |
| chapters/ch09.md | `## Chapter 9: Morse in the Moonlight` | ~6,400 | cw |
| chapters/ch10.md | `## Chapter 10: The Satellite Chase` | ~6,400 | satellite |
| chapters/ch11.md | `## Chapter 11: Field Day` | ~6,400 | fieldday |
| chapters/ch12.md | `## Chapter 12: When the Phones Went Down` | ~6,400 | storm |
| chapters/epilogue.md | `## Epilogue: Call Signs` | ~3,500 | starlight |
| appendices/junkbox-cookbook.md | `## Appendix A: The Junkbox Cookbook` | ~2,000 | — |
| appendices/glossary.md | `## Appendix B: Glossary for Young Builders` | ~1,500 | — |

## Per-chapter beats

### Prologue: The Radio in the Dumpster (POV Jun)
Late August, heat. Jun cuts behind Hackett's TV & Stereo (closing after 41 years) chasing
a dumpster full of "junk" and finds a Kenwood TS-520S — dented, dusty, beautiful. She
drags it home on her skateboard. Marisol: "Your grandfather's disease." Establish Jun's
salvage log, the FT-60R she inherited but barely understands, and the ache of Abuelo
Rudy never teaching her. She cleans the Kenwood, finds the blown fuse and the green
corrosion, and — not knowing what it really is yet — feels it pull her. Ends with the
school club-fair flyer: "AMATEUR RADIO CLUB — Room 114-B. (If we still exist.)"

### Chapter 1: The Club with Three Members (POV Jun)
Club fair: the sad card table. Mr. O explains the board rule (≥4 members + one public
demonstration by June, or Room 114-B is gone). Jun signs; drags Priya (skeptical: "it's
called the internet"); Theo signs for the audio gear; Bea signs without saying a word.
First meeting: Mr. O tunes his portable to 20 m at lunch and the room goes quiet —
voices sliding by, a station in Brazil, static like surf. Jun hauls in the TS-520S:
"It's dead." Mr. O: "Everything is, until you learn why." He mentions a man named Si
Webb who "knows antennas the way your grandfather knew people." Ends with the club
voting to resurrect itself — and Ms. Delgado witnessing the signup sheet with four names.

### Chapter 2: The Pop-Can Dipole (POV Jun)
October. They can't transmit (unlicensed) but they want to *hear* the repeater better —
and Si (first visit to the barn; Resistor; terrible coffee) sets the challenge: build an
antenna from this blue recycle bin. The pop-can dipole: four cans a side, broomstick,
coax, choke. Failure beat: first SWR is awful because Jun soldered the braid to the
wrong can / gaps uneven — they diagnose with Si's analyzer and fix the spacing. Theory:
wavelength, 468/f, resonance, why the can doesn't care it used to hold root beer.
Payoff: from the school roof with the FT-60R on receive they hear the Tuesday night net
clear as a bell — and Si, licensed, calls in with Jun holding the mic for one legal
third-party hello: "W7MR net, this is W7JUNK with a visitor." Jun says her name on the
air. Hooked. Ends: Si looks at the gray fall sky: "Wait till you hear what the *sky*
does. For that you need a wire."

### Chapter 3: Wire in the Walls (POV Jun)
November. The TS-520S revival (fuse holder, contact cleaner, the smell of old dust on
warm tubes — it lives) becomes the club heart. But it needs a real antenna: the
extension-cord dipole, 20 m, 16.6 ft a leg, choke balun, inverted-V off the flagpole
(permission saga with Ms. Delgado; the custodian **Mr. Abernathy** rigs the halyard
safely — spotter rules stated in-story). Failure beat: SWR sky-high until Priya finds
they measured with the velocity factor *inside* the leg length math wrong — no, canon:
they cut for 14.300 (phone band edge wrong) and it tunes best low; they trim to 14.100.
Theory: resonance, SWR, why a balun, why height matters. Payoff: first HF contact —
Mr. O at the mic, Denver station, then Theo tries his voice and a station in Texas says
"you're 59 into Austin." They log it. Ends: Si: "You put a wire in the sky and the sky
answered. Now — who wants to hunt a hidden transmitter?"

### Chapter 4: The Tape-Measure Yagi (POV Jun)
December, light snow. Fox hunt in Fairview County Park. Build: WB2HOL tape-measure
yagi — measuring twice, the snap of a retracting tape, PVC tees, hose clamps, hairpin
match; failure beat: bearings are nonsense until they add the 7-turn choke behind the
reflector (feedline pickup). Theory: directivity, gain, dB, front-to-back, nulls.
Payoff: two teams — Jun+Priya vs Theo+Bea; Theo cheats by driving (caught, funny);
Jun's team finds the ammo-can fox behind the sledding hill in 41 minutes; the fox IDing
in Morse is the first time Bea *hears* code as music. Ends: Bea asks Si, very quietly,
"Could a person learn that?" — plants Ch9. Snow on the yagi like icing.

### Chapter 5: The Night the Sky Opened (POV Jun)
January. Si invites them for a gray-line session at the farm. Theory in the truck:
D/E/F2 layers, MUF, cycle 25, why dusk is magic on 10 m. They hang a 10-m dipole
(16.5 ft — "an antenna you could lose in a laundry basket") between Si's oaks. Failure
beat: at first nothing — the band sounds dead; patience; then the wall of static lifts
like a curtain at sunset. Payoff: JA1YMK, Takeshi in Osaka, sunrise tomorrow over the
Pacific; Jun, shaking, gives a 55 report with Mr. O supervising (control-operator rules
stated plainly); then VK2KDP. Starlight overhead; copper wire glowing faint in the
floodlight. **Title moment**: Jun thinks of the book of her abuelo's photos — a wire on
a roof at dusk — "copper wire and starlight." Ends: Si: "That's the sky opening. It
closes, too. Everything about this hobby is weather." — plants storm arc.

### Chapter 6: Slinkies and Loop-the-Loop (POV Jun)
February. Bea's problem: Pinewall lease, no antennas, Babcia's rules, winter. The club
conspires to build her something invisible. Two builds: the attic Slinky dipole (works,
barely, through a tuner — canon compromise honesty) and the 3-ft copper magnetic loop
with the salvaged AM-radio capacitor, which lives on her balcony disguised as a "plant
stand sculpture" (PVC painted, very HOA). Failure beat: the loop won't tune past 20 m
until Priya adds the padding capacitor — bandwidth so narrow you retune every few kHz.
Theory: efficiency vs. size, why small loops are current machines, tuner vs. resonance.
Payoff: Bea hears (receive-only) a 40-m roundtable from her bedroom floor — her first
*own-antenna* reception — and grins the first real grin of the book. Ends: Babcia
caught her — and instead of anger, brings pierogi to the next meeting. ("Your
grandfather talked to ships," she says of her late husband. New canon: he was a radio
officer in the merchant marine — never contradict this.)

### Chapter 7: The J-Pole and the Storm (POV Jun)
March. The club needs a permanent 2-m home: the copper J-pole. Build with Si's pipe
cutter and the 705/f math; solder the tee; feed-point hunt (2–3 in, watching the
analyzer); mount on the school's flat roof on a scavenged tripod — with the safety
litany done as action (spotters, twice-the-length from power lines, disconnect in
weather). Theory: verticals, ground planes, why the J matches itself, lightning
discipline. Payoff + turn: the same week, a March squall line; they listen (not
transmit) to the Skywarn net on the new J-pole while Si reports from his grounded
station; a funnel cloud report comes from *their side of town* and they watch the net
work like a machine. Respect seeded: radio as public service. Ends: Mr. O: "You don't
build antennas *for* storms. You build them *before* storms." — plants Ch11–12.

### Chapter 8: The RFI Detective (POV Jun)
April. Mr. Pruitt storms in: his powered speakers buzz every time "you kids play radio"
(the club now transmits under Mr. O's supervision from 114-B after school — canon: the
TS-520S + extension-cord dipole). Detective story: they log times, map the interference,
find it's the cheap unshielded speaker leads acting as antennas + common-mode current on
their own coax. Builds: snap-on ferrite chokes for Pruitt's cables; a proper 1:1 choke
and station ground for the shack; bonding the rig/tuner ground bus. Failure beat: they
fix their end and it's *still* there — until they find the second path (Pruitt's
turntable preamp). Theory: RFI, common-mode currents, why chokes work, grounding vs.
bonding. Diplomacy payoff: Pruitt, ex-DJ, brings records and stays for coffee; becomes
the club's first fan. Ends: he says "You want problems? Try keeping a tower up through
Field Day." Everyone looks at everyone. Field Day.

### Chapter 9: Morse in the Moonlight (POV **Bea**)
Late April. Bea's chapter. Si gives her the J-38 key and a battered code-practice
oscillator the club builds from a kit (NE555 — one soldering evening). The EFHW build at
Si's: unspooling magnet wire from the dead transformer, winding the 49:1 unun (2:14 on
the FT240-43), 65.5 ft from oak to barn, 6.5-ft counterpoise. Failure beat: the unun
gets hot and signals are mush — they'd wound it with the wrong turn ratio / twisted the
wrong wires together; rewind; 1.4:1. Theory: resonance and harmonics, why 49:1, why CW
gets through when voice can't (bandwidth, power density). Payoff: full moon; Bea, on
receive with Si keying slow Morse at her elbow, copies her name; then, licensed
control-operator setup, Si calls a slow-speed (SKCC-style) CQ and Bea sends "BEA" at 8
wpm to a patient ham in Idaho who sends back "FB OM" — she laughs out loud, alone with
the moon and the wire. Ends: she dreams in dit-dah; school is a countdown to night.

### Chapter 10: The Satellite Chase (POV **Theo**)
May. Theo's chapter — the showboat learns precision. App-tracked passes; the
tape-measure yagi returns; Doppler (±3.5 kHz, tune down through the pass); failure
beat: first pass they hear *nothing* — pointing with the headphones cord tangled,
polarization wrong, uplink vs downlink confusion; Priya makes a pass checklist.
Payoff: second pass — the ISS downlink 145.800 alive, an astronaut's voice packet /
schools contact heard from the parking lot on a $6 antenna; then they digipeat a packet
through the ISS and see it gated to the internet — Theo, who thought space was for
billionaires, talks to a *machine in orbit* with a tape measure. Ends: the school
announces Field Day public-demo approval (Ms. Delgado arc) — the club's demonstration
will be Field Day itself, open to the public. Countdown begins.

### Chapter 11: Field Day (POV Jun)
27–28 June, Fairview County Park. The full arsenal deployed in one glorious junkyard
spread: extension-cord dipole, 10-m wire, EFHW, J-pole on the tripod, pop-can dipole
for talk-in, tape-measure yagi on satellite watch; battery + a borrowed solar panel;
the TS-520S + Si's IC-7300; class 2A as N8OWL. Set-pieces: the public demo (Ms. Delgado
brings the school board chair; kids make fox hunts with the yagi); Theo runs SSB pileups
like a DJ until he melts down (humility beat); Bea's CW rate stuns everyone; midnight:
the storm cell — wind, the County Tech crank-up tower cranking down in a hurry, and the
club's low, lashed-down junk antennas *still up*; they shelter, disconnected, discipline
from Ch7 paying off; after the cell passes they get back on and work the graveyard
shift — Priya's gray-line theory pays at dawn with a JA run on 10 m. Ends: sunup,
coffee, 312 QSOs in the log, and the board chair asking, "Is it always like this?"

### Chapter 12: When the Phones Went Down (POV Jun)
The week after Field Day. The same storm system had dropped a tornado two counties
over; aftermath ripples: a second severe line hits Maple Run — power out, cell towers
overloaded/down, sirens. The club, with Si and Mr. O, opens a health-and-welfare net
from Si's farm (grounded, generator) relaying for the county; the school's J-pole is
checked *after* the storm (discipline), the pop-can dipole rides in a go-kit; set-piece:
they pass a message for Mrs. Abernathy (custodian's wife) to her sister in Denver —
"we are fine, tell Mom we're fine" — and the reply comes back at dawn. Theo runs net
control steady now. Media: the local paper's photo is the pop-can dipole in a
five-gallon bucket. School board meeting: Ms. Delgado, Pruitt, Abernathy, the board
chair from Field Day; the club is made permanent — and given the Room 114-B key, and a
line item: "$400. Antenna fund." Laughter: they spent $38 all year. Ends: Si, quietly,
to Jun: "Your grandfather would like this." Jun: "He built half of it." (Metaphor — the
HT, the itch — don't overplay.)

### Epilogue: Call Signs (POV Jun)
August 2026, one year after the dumpster. VE session in the library: all four pass
Technician (Bea also passes General — she's insatiable). Waiting on the FCC database
like waiting for a comet; the calls appear: KI7JUN, KI7BEA, KI7PNA, KI7TOM. That
evening at Si's meadow: the extension-cord dipole now lives there as a "memorial" —
no, canon: Si kept the club's first 20-m extension-cord dipole and re-hung it between
his oaks "for the newest hams." Jun, with her own call, her abuelo's HT clipped to her
belt, sits at the IC-7300 as dusk comes on — gray line, of course — and sends her first
solo CQ on 10 m as the stars come out. Answer comes back (leave the station vague —
someone's tomorrow). Final beat mirrors the Prologue: a wire, the sky, a voice.
"Copper wire and starlight" lands once, earned, quiet.

### Appendix A: The Junkbox Cookbook
One-page recipe per antenna, written in the book's voice (second person, warm, precise,
safe): pop-can dipole; extension-cord 20-m dipole; tape-measure yagi; Slinky attic
dipole; salvaged-capacitor magnetic loop; copper J-pole; EFHW with 49:1 unun. Each:
parts (with "trash source" hints), dimensions from the canon table, steps, tuning,
safety notes, and one "why it works" paragraph. Open with the safety litany (power
lines, lightning, spotters, RF sense). Real numbers only — match the chapters.

### Appendix B: Glossary for Young Builders
~45 terms, one or two sentences each, in the book's voice (compare the storybook's
glossary tone but older): antenna, dipole, feedline/coax, balun/unun/choke, SWR,
resonance, wavelength/frequency, bands (HF/VHF/UHF), ionosphere, skip/skywave, gray
line, MUF, gain, dB, directivity, polarization, ground plane, magnetic loop, tuner,
repeater/offset/PL, net, Skywarn, RFI, ferrite, grounding/bonding, CQ, call sign,
phonetics, RST, QSL card, DX, CW/Morse, QRP, Field Day, Elmer, silent key, 73.

## Style laws (prose)

- Sentences with rhythm; technical terms used correctly and casually, defined once in
  context. No walls of exposition: max two paragraphs of theory before someone *does*
  or *says* something.
- Dialog carries character: Priya precise and dry; Theo performs; Bea says little and
  means all of it; Jun notices materials and weather; Si aphorisms, short, never sappy;
  Mr. O deadpan teacher-isms.
- Each chapter opens mid-scene (no "It was a..." weather openings except the Prologue's
  heat, which is characterful) and ends on a forward-looking human beat.
- Use `---` scene breaks liberally (3–6 per chapter).
- The words "magic" (at most twice in the whole book, both earned), "suddenly", and
  "little did they know" are banned. No deus ex machina: every win is built, literally,
  earlier in the book.
- Never contradict the canon tables. All call signs fictional. All math right.
