# One Star, Five Stars for the Food

[![make.fun competition](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![rank](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/epanpai/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/rank.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![reward](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/epanpai/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/reward.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)

Entry for the [make.fun](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7) bounty **One Star, Five Stars for the Food** ($2 pot, free entry).

## The entry

> I flew nine light-years for one star: the air tastes of exhaust, the locals queue for bitter bean water, and yet the dumplings made my third stomach weep with joy.

One sentence, 163 characters — an alien tourist's one-star review of Earth that still slips in a real compliment about the food. It opens with the verdict and the alien scale in one breath ("nine light-years for one star"), gives two grievances only an outsider would notice (air that tastes of exhaust, locals queuing for bitter bean water), then turns on "and yet" to a specific food (dumplings) with a bodily alien kicker: a third stomach weeping with joy.

## How it works

`main.py` (Python 3, standard library only) writes that single sentence to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Before writing it self-checks the competition gate: UTF-8 text of 1–200 characters, not whitespace-only, exactly one sentence on a single line — then reads the file back and verifies it byte-for-byte.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```
