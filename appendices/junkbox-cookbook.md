## Appendix A: The Junkbox Cookbook

Every antenna in this book was built by kids with more curiosity than money, out of things the world threw away — and every one is written down here the way recipes should be: parts, steps, tuning, and why it works. If you've read the story, you've watched each of them fail once and go on the air.

The trash sources are real: the club found these things in these places, and your town has the same bins. Ask before you take; ask before you cut. As for the law — building and listening need no license, and listening is always free. Transmitting takes a license and a control operator, which is what clubs and license classes are for. Build first. The license follows.

### Read This First: The Rules

Si Webb made the club recite these before he let them touch a ladder, and now they're yours.

1. **Power lines: twice the length, every time.** An antenna goes up at least twice its own length from any power line, so if it falls, it falls short. Assume every wire on every pole can kill you; you'll be right often enough.
2. **Lightning: disconnect and wait.** At the first thunder, unplug the coax and do not operate until the storm has passed. Not "is passing." Passed. The club watched the Skywarn net from Si's grounded station, sitting on their hands.
3. **Nothing goes up without a spotter.** Ladders, roofs, flagpoles, trees: one person climbs, one person watches. Nobody remembers a safe day as a boring one.
4. **RF is weather too.** Five watts from a handheld is fine; a hundred watts into an HF antenna is a different climate, and nobody stands next to it while it transmits. Hands off the magnetic loop's capacitor whenever the push-to-talk is down.

---

### 1. The Pop-Can Dipole (2 meters)

The antenna that started everything: eight soda cans and a broomstick, and the Tuesday night net came in clear as a bell.

**You will need:**

- 8 empty soda cans, rinsed (trash source: any recycling bin — the blue one behind a school cafeteria is a proven vein)
- A wooden broomstick or 4-foot dowel (trash source: one broken broom)
- 10–15 feet of RG-58 coax (trash source: hamfest bargain boxes)
- Tape, zip ties, sandpaper, and two ring lugs with small nuts and bolts (or sheet-metal screws) for the feed connections

**Build:**

1. Sand a coin-sized patch of paint off two cans — the feed cans. Fair warning: you cannot solder to aluminum cans (the club learned this so you don't have to). Crimp a ring lug on each coax conductor and bolt or screw each lug to a bare sanded patch instead.
2. Lash four cans to the stick, mouth-to-base, then four more on the other side, with a 1-inch gap between the two inner cans. Four 4.83-inch cans is 19.3 inches a side — not a coincidence.
3. Attach the coax at the gap: center conductor's lug to one feed can, braid's lug to the other. Bolts tight, patch bare, then tape over the hardware.
4. Coil a 4-turn choke in the coax right at the feedpoint. Mount it vertical, away from bodies.

**Tuning:** Slide the can stacks until the SWR dips near mid-band; the club's best was about 1.8:1 — under 2:1 is fine. From the school roof it hit W7MR/R at 146.760 like it was made for it.

**Why it works:** Each four-can stack is a quarter-wave at 146 MHz; two quarter-waves back to back make a half-wave dipole. The can doesn't care it used to hold root beer — electrons only care about shape and size. The choke keeps RF off the outside of the coax, so your feedline doesn't join the antenna.

---

### 2. The Extension-Cord Dipole (20 meters)

The antenna that put the club on HF — a hundred-foot extension cord, promoted.

**You will need:**

- One 100-foot outdoor extension cord (trash source: garage sales, thrift-store as-is bins — ask before cutting one that still works)
- About 50 feet of RG-58 coax
- Center and end insulators — scrap cutting board, PVC, a cut-up milk jug
- Nylon rope; zip ties, solder, coax seal

**Build:**

1. Do the math: total length in feet is four sixty-eight divided by the frequency in megahertz. For 14.100 MHz, that's 33.2 feet — two 16.6-foot legs. Cut them a foot long; you'll trim.
2. Skin the inner ends, attach the legs to the center insulator, and solder on the coax: center to one leg, braid to the other. Weatherproof it like you mean it.
3. Coil the coax into 8 turns, 6 inches across, right below the feedpoint — your 1:1 choke balun.
4. Hang it as an inverted-V: the club used the flagpole cleat, about 28 feet up, with permission and a spotter, legs sloping to ends about 12 feet off the ground.

**Tuning:** Fold the ends back a few inches at a time — folding beats cutting — until the SWR dip sits at 14.100. The club's first try was cut for 14.300 and tuned low; their reward for trimming was 1.6:1 mid-band, Denver, and a voice in Texas telling Theo he was 59 into Austin.

**Why it works:** At resonance a half-wave dipole is exactly the load your radio was built for, so power leaves instead of bouncing back. And height is free gain: a wire 28 feet up at 14 MHz isn't a wire. It's a door.

---

### 3. The Tape-Measure Yagi (2 meters)

The fox hunter — and later the antenna that heard the space station. The classic WB2HOL design, about six dollars if you're bad at scrounging.

**You will need:**

- A 1-inch × 25-foot steel tape measure (trash source: a dead one with a broken spring — you only want the blade)
- About 5 feet of 3/4-inch PVC pipe and two cross-tees (trash source: construction offcuts — ask politely)
- Four hose clamps (trash source: the rusty coffee can of them in somebody's garage)
- Stiff wire for the hairpin; 10 feet of RG-58; gloves, tape, zip ties

**Build:**

1. Gloves on — cut tape edges are razors. Cut a 41 3/8-inch reflector, two 17 3/4-inch driven-element pieces, and a 35 1/8-inch director.
2. Clamp the elements across the boom: reflector near one end, driven element 8 inches in front of it, director 12 1/2 inches beyond the driven.
3. Face the driven pieces at each other with a 1-inch gap, scrape to bare metal, solder coax center to one and braid to the other, and bridge the gap with the hairpin.
4. For fox hunting, coil 7 turns of coax behind the reflector — skip it and feedline pickup makes your bearings lie.

**Tuning:** Forgiving design — the club built theirs with snow on the picnic table. High SWR means the hairpin, the gap, or unscraped coating.

**Why it works:** The driven element radiates; the longer reflector pushes the signal forward, the shorter director pulls it. That beam is worth about 7 dBd — and since 3 dB is a doubling, that's your handheld multiplied several times over in one direction. The null behind finds the fox: sweep, listen for where the signal *isn't*, and walk until there's an ammo can at your feet, IDing in Morse.

---

### 4. The Slinky Attic Dipole (40 meters)

For every kid with a strict lease, a no-antennas landlord, or a Babcia. The honest antenna: it works, barely — and "barely" is the whole lesson.

**You will need:**

- Two metal Slinkies — real steel, not plastic (trash source: thrift-store toy bins; a cousin's toy box, in a fair trade)
- Coax enough to reach the radio; cup hooks and string
- An antenna tuner (borrowed counts)

**Build:**

1. Stretch each Slinky to about 10 feet — taut, not tight — along attic rafters, clear of house wiring and ductwork.
2. Join the inner ends at a rafter: coax center to one Slinky, braid to the other.
3. Run the coax to the radio through the tuner. There is no step four. That's the appeal.

**Tuning:** Resonant nowhere polite, so the tuner does the lifting — the club's loaded up on 40 meters from a bedroom floor. Keep the power modest: this one lives indoors with you.

**Why it works:** A stretched Slinky is a helically wound wire — the coiling packs inductance into a short space, electrically longer than it looks — and the tuner coaxes the rest into submission. Twenty feet of spring is a fraction of the 65.5 feet a 40-meter dipole wants, so it radiates like a short person reaching a high shelf — with effort. Any antenna beats no antenna. Ask Bea, who heard a 40-meter roundtable through two toys and grinned the first real grin of the book.

---

### 5. The Salvaged-Capacitor Magnetic Loop (40–20 meters)

The loop that lived on Bea's balcony disguised as modern sculpture.

**You will need:**

- About 9.4 feet of 3/4-inch copper pipe (trash source: plumber offcuts, HVAC scrap bins — pocket change by weight)
- A variable capacitor, about 365 pF, from a dead AM radio (trash source: any dead AM clock radio — the tuning capacitor inside is the treasure)
- A fixed padding capacitor from the same radio
- A copper strip and small capacitor for the gamma match; a plastic box; a stand

**Build:**

1. Bend the pipe into a circle 3 feet across — joint soldered tight; every joint matters.
2. Bridge a gap at the top with the variable capacitor, padding capacitor in parallel.
3. Rig the gamma match at the bottom: a short strip parallel to the loop, fed by the coax. Weatherproof the box.
4. Mount it where it can turn, clear of metal and of people.

**Tuning:** Bandwidth is about 15 kHz, so you retune every few kHz. Turn the capacitor for maximum band noise on receive, then check SWR at low power. Won't reach 40 meters? More padding capacitance — that was Priya's fix. Hands off the capacitor while transmitting — even a few watts means serious voltage across those plates.

**Why it works:** A 3-foot loop is about 0.09 wavelengths on 40 meters — preposterously small — and it works because a small loop is a current machine: radiation comes from a large current around a small circumference. The capacitor cancels the loop's inductance and tunes it to resonance; the price is razor bandwidth, the reward an antenna the size of a bicycle wheel that hears like something ten times bigger. Physics doesn't care what your lease says. Physics isn't on the lease.

---

### 6. The Copper J-Pole (2 meters)

The club's permanent roof antenna — the one that heard the Skywarn net work like a machine. Build it *before* the storm.

**You will need:**

- About 7 feet of 1/2-inch copper pipe (trash source: plumber offcuts, the scrap yard by the pound)
- A 1/2-inch tee, an elbow, short nipples; pipe cutter, torch, solder, flux — borrow a grown-up and the torch as a set
- 10 feet of RG-58; two small hose clamps or solder lugs
- A tripod (trash source: a dead camera tripod or a curbside dish mount)

**Build:**

1. Do the math: the radiator is a half-wave — seven-oh-five divided by the frequency in megahertz, in feet. For 146 MHz that comes out to 4.83 feet — just about 58 inches — so cut 57½ inches and let the analyzer find the last eighth. Cut the stub at 19 inches.
2. Sweat the J together: stub and radiator parallel, about 1¾ inches apart, joined at the bottom. Let it cool; admire it — everyone does.
3. Attach the coax 2 inches above the crossbar: center to the long side, braid to the stub side.
4. Coil 4 turns of coax, 5 inches across, at the feedpoint for a choke. Weatherproof everything.

**Tuning:** Slide the feed connections between 2 and 3 inches until the dip lands mid-band, then make them permanent. Mount it vertical, up high, twice its length from any power line.

**Why it works:** The clever part is the stub: a half-wave radiator fed at its end presents a high, unfriendly impedance, and the quarter-wave stub transforms it down to something your coax likes. No ground plane, no radials — a half-wave vertical that matches itself. Put one on a roof and a school hears the whole county — including, come March, the net that matters.

---

### 7. The End-Fed Half-Wave with a 49:1 Unun (40 meters, and friends)

Bea's moonlight antenna — one wire, four bands, no tuner on a good day.

**You will need:**

- 65.5 feet of enameled magnet wire (trash source: unspooled from a dead power transformer — get a grown-up to help extract it, and leave microwave capacitors strictly alone)
- One FT240-43 ferrite toroid (the one honest purchase here — a few dollars online or at a hamfest)
- Extra magnet wire, a small box, an insulator, rope; a 6.5-foot counterpoise wire; coax

**Build:**

1. Wind the unun: fourteen turns on the toroid, with a two-turn primary alongside the first two of them — the 2:14, and the ratio is the whole trick. Count out loud — the club's first unun ran hot on a twisted winding; the rewind gave 1.4:1.
2. Primary across the coax, center and braid; the fourteen-turn winding between antenna wire and counterpoise.
3. Attach the 65.5-foot radiator — a half-wave at 7.150 MHz, four sixty-eight over the frequency again.
4. Attach the 6.5-foot counterpoise; let it dangle or lie along the ground.
5. String the radiator high and in the clear — tree to barn, house to pole. The sky is forgiving.

**Tuning:** Trim for 40 meters first — fold the far end back a few inches at a time — and the harmonics follow: 20, 15, and 10 come along for free. If the unun warms on transmit, stop and recount the turns.

**Why it works:** A half-wave wire is resonant wherever you feed it; fed at the end, the impedance runs to a couple of thousand ohms, far above your coax's 50. The turns ratio, fourteen to two, is seven, and seven squared is forty-nine: the unun steps 50 ohms up to meet it. The short counterpoise — 0.05 wavelengths — gives the return current somewhere to be.

---

That's the whole year — seven antennas, one blue bin at a time. Build any one of them. And when a voice comes back out of the sky at you — it will — you'll understand why the club kept the pop-can dipole long after they didn't need it anymore.

73 — and see you on the air.
