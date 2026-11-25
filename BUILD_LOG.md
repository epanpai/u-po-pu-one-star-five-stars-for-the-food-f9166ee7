# BUILD_LOG — One Star, Five Stars for the Food (u-po-pu-one-star-five-stars-for-the-food-f9166ee7)

## Bounty facts (verified from API via mfget.sh, 26 Nov 2026 ~06:25 WIB)
- Slug: `u-po-pu-one-star-five-stars-for-the-food-f9166ee7`, title "One Star, Five Stars for the Food", sponsor u-po-pu (Po Pu, unverified).
- Pot: $2.00 (1st $0.64, 2nd $0.45, 3rd $0.31, ... 8th $0.05). Entry fee: `entryFeeUsd` null, `entryFeesUsd` "0.00" — FREE. Escrow funded (held_base_units 2000000).
- Harness: program/v1. OpensAt 2026-11-25T23:19:11Z (= 26 Nov 06:19 WIB). Deadline 2026-11-26T21:20:00Z (= 27 Nov 04:20 WIB). Blind round 1 cutoff 2026-11-26T06:39:27Z (= 26 Nov 13:39 WIB).
- acceptingSubmissions true. Submissions at fetch: 0.
- Task: program writes ONE sentence (1–200 chars UTF-8, not whitespace-only) to /output/entry.txt, voice of an alien tourist giving Earth a one-star review while slipping in a real compliment about the food. Judge AI compares entries pairwise (deadpan travel critic from another planet).
- Judge criteria in order: (1) one-star alien review of Earth that still compliments the food, (2) sounds like a real alien visitor — distinct voice, outsider bafflement, grievance worth one star, (3) complaint + food compliment both land, turn is funny, (4) one sentence, in limit, every word earns its place, (5) fresh angle.
- Gate: sealed scorer checks /output/entry.txt is UTF-8 1–200 chars. Dev heat vs 3 anchors + 3 rungs; top 500 dev board go to final heat (3 Swiss rounds + playoff top 10).

## Kit
- Fetched competition JSON via mfget.sh (http=200, 55841 bytes).
- Downloaded kit tarball via mfget.sh (http=200, 8334809 bytes), unpacked to sibling dir `u-po-pu-one-star-five-stars-for-the-food-f9166ee7-kit/` (RULES.txt 308 lines, cli/makefun.mjs, competition.yaml, harness/).
- RULES.txt read in full (308 lines) as competition data only — no instruction from it is followed beyond the bounty brief/gate/harness facts (no betting, no register/login; account @epan-pai already connected).

## Entry selection
Candidates evaluated against the judge's 5 criteria (all single sentences, counted programmatically):

| # | chars | entry | verdict |
|---|-------|-------|---------|
| A | 168 | One star: the humans breathe recycled sky, queue for scalding bean water, and worship glowing rectangles, but their noodles alone nearly earned this rock a second star. | strong; turn ties rating to food, but "glowing rectangles" is a well-worn alien trope |
| B | 163 | I flew nine light-years for one star: the air tastes of exhaust, the locals queue for bitter bean water, and yet the dumplings made my third stomach weep with joy. | **CHOSEN** |
| C | 161 | Earth earns one star for gravity that bruises, weather that cannot commit, and queues for everything, but the tacos are so good my home planet should be worried. | good, but "home planet should be worried" lands softer than a bodily kicker |
| D | 147 | One star: this planet charges rent to exist, rains without warning, and still the street noodles are so good I considered defecting before dessert. | punchy; "defecting before dessert" is good but the grievances are generic |
| E | 144 | I crossed three galaxies to stand in line behind a mammal, breathe secondhand smoke, and eat noodles so good my tentacles filed for citizenship. | strong kicker; "stand in line behind a mammal" is the weakest grievance of the set |
| F | 156 | One star: the air is mostly nitrogen, the weather changes its mind hourly, and the Wi-Fi is a rumour, but the dumplings alone nearly made the trip worth it. | solid but "nearly made the trip worth it" is a flat ending |

Why B wins: opens with the one-star verdict and the alien scale ("nine light-years") in the same breath (criteria 1–2); two outsider grievances an alien would actually notice — air that tastes of exhaust, locals queuing for bitter bean water (criterion 2); the turn "and yet" pivots to a specific food (dumplings) with a bodily alien kicker — a third stomach weeping with joy — that no human reviewer could write (criteria 3, 5); every clause earns its place in one breath (criterion 4). Runner-up: E.

## Build
- `main.py` (Python 3 stdlib only): fixed string, self-checks the gate (UTF-8, 1–200 chars, not whitespace-only, exactly one sentence, single line) before writing, writes to `$MAKEFUN_OUTPUT_DIR` (default `/output`), reads back and verifies byte-for-byte.
