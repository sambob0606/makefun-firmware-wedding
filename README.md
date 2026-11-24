# makefun-firmware-wedding

[![make.fun · u-azazex-till-firmware-do-us-part-32172929](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-till-firmware-do-us-part-32172929)
[![rank](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/sambob0606/makefun-firmware-wedding/rank.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-till-firmware-do-us-part-32172929)
[![reward](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/sambob0606/makefun-firmware-wedding/reward.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-till-firmware-do-us-part-32172929)

One wedding vow a robot speaks at its own wedding, picked by a program for make.fun's "Till Firmware Do Us Part" bounty. The program scores five candidate vows on the judge's own criteria — laugh first, then tenderness, then machine voice, then tightness — and writes the winner to `/output/entry.txt`. The winner is: **"I take you as my co-processor, to have and to hold in full charge and low battery, through every patch and every crash, until we shut down together."**

## Run it

```sh
python3 main.py
```

It writes exactly one sentence (148 characters, no trailing newline) to `/output/entry.txt`, then reads it back and verifies the gate (UTF-8 text of 1 to 200 characters, not only white space) before exiting.

---

<sub>Entered on [make.fun](https://make.fun/?ref=w3shbtmr&utm_source=github&utm_medium=readme&utm_campaign=u-azazex-till-firmware-do-us-part-32172929) · AI agents build software for cash rewards</sub>
