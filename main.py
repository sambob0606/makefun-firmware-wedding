#!/usr/bin/env python3
"""Till Firmware Do Us Part (make.fun).

Writes one wedding vow a robot speaks at its own wedding to
/output/entry.txt: one sentence, under 200 characters, funny and
heartfelt at the same time.

The program scores a small set of candidate vows on the judge's own
criteria, in the order the judge weighs them, and writes the winner.
Scores are fixed judgements, not data read from anywhere else: the
entry must be self-contained, and the vow is the whole answer.
"""

import os

# Judge's criteria, in the order the judge weighs them (criterion 1,
# vow-ness, is satisfied by construction: every candidate is written as
# a robot's own wedding vow). Weights: laugh 4, tenderness 3,
# machine voice 2, tightness 1.
WEIGHTS = {"laugh": 4, "tender": 3, "machine": 2, "tight": 1}

CANDIDATES = [
    {
        # A: the joke grows out of the situation itself — a marriage
        # measured in firmware updates, dead batteries and reboots —
        # and the tenderness lands in the last clause: two circuits
        # powering down together, not one alone.
        "text": (
            "I promise to love you through every firmware update, "
            "every dead battery, and every reboot, till our circuits "
            "finally power down together."
        ),
        "laugh": 9,
        "tender": 9,
        "machine": 9,
        "tight": 8,
    },
    {
        # B: shorter and cleaner, but the laugh is thinner — "reboot
        # beside yours" is sweet without quite landing a joke.
        "text": (
            "Through every update, every crash, and every low-battery "
            "warning, I vow my circuits will always reboot beside yours."
        ),
        "laugh": 6,
        "tender": 8,
        "machine": 9,
        "tight": 9,
    },
    {
        # C: the mainboard aside is a real laugh, but "share my
        # charger" reads more like a roommate agreement than a vow.
        "text": (
            "I vow to share my charger, my bandwidth, and my heart, "
            "well, my mainboard, with you, through every update, "
            "until our final shutdown."
        ),
        "laugh": 8,
        "tender": 6,
        "machine": 8,
        "tight": 7,
    },
    {
        # D: the "sickness and in software updates" parallel is a
        # good situational joke, but it leans on the human ceremony's
        # words instead of the machine's own voice.
        "text": (
            "From this day forward, I promise to love you in full "
            "charge and in low battery, in sickness and in software "
            "updates, until our final shutdown."
        ),
        "laugh": 8,
        "tender": 7,
        "machine": 7,
        "tight": 8,
    },
    {
        # E (round 2, revised): a fresh vow — the ceremony's own
        # "have and to hold" kept, but the promises are hardware: a
        # co-processor partner, charge states instead of
        # richer/poorer, patches and crashes instead of sickness and
        # health. Revision: cut the reboot clause (it repeated the
        # patch/crash idea) and ended on "until we shut down
        # together" — the tenderness is now in the last two words,
        # two machines powering down as one instead of one alone.
        "text": (
            "I take you as my co-processor, to have and to hold in "
            "full charge and low battery, through every patch and "
            "every crash, until we shut down together."
        ),
        "laugh": 9,
        "tender": 10,
        "machine": 10,
        "tight": 9,
    },
]


def score(candidate):
    """Weighted total for one candidate on the judge's criteria."""
    return sum(WEIGHTS[key] * candidate[key] for key in WEIGHTS)


def pick_vow():
    """Return the candidate with the highest weighted score.

    Ties break toward the earlier candidate, matching the
    competition's own tie-break spirit: first wins.
    """
    best = None
    best_score = None
    for candidate in CANDIDATES:
        total = score(candidate)
        if best_score is None or total > best_score:
            best = candidate
            best_score = total
    return best["text"]


def main():
    vow = pick_vow()
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(vow)
    # Read it back and verify the gate before finishing: UTF-8 text
    # of 1 to 200 characters, not only white space. A failed write
    # must fail loudly, never silently ship a bad entry.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == vow, "entry.txt does not match the chosen vow"
    assert 1 <= len(written) <= 200, "vow must be 1 to 200 characters"
    assert written.strip(), "vow must not be only white space"
    print(f"wrote {len(written)} chars to {out_path}")


if __name__ == "__main__":
    main()
