#! /usr/bin/env python3
import contextlib
import csv
import random

BRVTAL = {"Death Metal", "Black Metal", "Doom Metal", "Grind"}
NOT_BRVTAL = {"Heavy Metal", "Progressive Metal", "Power Metal", "Melodic Death Metal",
        "Folk Metal", "Post-metal", "Hard Rock", "Not Metal", "Avante Garde",
        "Progressive Death", "Thrash Metal"}
brvtal_total = 0
not_brvtal_total = 0
both_total = 0
neither_total = 0

black_total = 0
death_total = 0

good_total = 0
bad_total = 0
good_all_total = 0
bad_all_total = 0

with contextlib.ExitStack() as stack:
    fi = open("data/info.csv", newline="")
    fo_brvtal = open("data/brvtality.csv", "w", newline="")
    fo_brvtal_all = open("data/brvtality_all.csv", "w", newline="")
    fo_black_death = open("data/black_death.csv", "w", newline="")
    fo_good = open("data/good.csv", "w", newline="")
    fo_good_all = open("data/good_all.csv", "w", newline="")

    data = csv.DictReader(fi)
    brvtal = csv.DictWriter(fo_brvtal, ["name", "label"])
    brvtal.writeheader()
    brvtal_all = csv.DictWriter(fo_brvtal_all, ["name", "tags"])
    brvtal_all.writeheader()
    black_death = csv.DictWriter(fo_black_death, ["name", "tags"])
    black_death.writeheader()
    good_bad = csv.DictWriter(fo_good, ["name", "tags"])
    good_bad.writeheader()
    good_bad_all = csv.DictWriter(fo_good_all, ["name", "tags"])
    good_bad_all.writeheader()

    for row in data:
        genres = set(row["Genres"].split("|"))

        is_brvtal = bool(genres & BRVTAL)
        is_not_brvtal = bool(genres & NOT_BRVTAL)
        if is_brvtal == is_not_brvtal:
            if is_brvtal:
                both_total += 1
            else:
                neither_total += 1
            # if it's in both categories or neither, skip it
            brvtality = None
        elif is_brvtal:
            brvtality = "brvtal"
            brvtal_total += 1
        else:
            brvtality = "not_brvtal"
            not_brvtal_total += 1
        if brvtality is not None:
            brvtal.writerow({"name": row["Art URL"], "label": brvtality})
        tags = []
        if is_brvtal:
            tags.append("brvtal")
        if is_not_brvtal:
            tags.append("not_brvtal")
        brvtal_all.writerow({"name": row["Art URL"], "tags": " ".join(tags)})

        if "Black Metal" in genres and "Death Metal" not in genres:
            black = "black"
            black_total += 1
        elif "Black Metal" not in genres and "Death Metal" in genres:
            black = "death"
            death_total += 1
        else:
            black = None
        if black is not None:
            black_death.writerow({"name": row["Art URL"], "tags": black})
            black = "black"

        score = float(row["Score"])
        if score > 4.0:
            good = "good"
            good_total += 1
        elif score < 2.5:
            good = "bad"
            bad_total += 1
        # hack: sample some 2.5s to make up numbers (we want ~ as many in each category)
        elif score == 4.0 and random.random() > 0.5:
            good = "good"
            good_total += 1
        else:
            good = None
        if good is not None:
            good_bad.writerow({"name": row["Art URL"], "tags": good})

        if score > 2.75:
            good = "good"
            good_all_total += 1
        elif score < 2.75:
            good = "bad"
            bad_all_total += 1
        else:
            good = None
        if good is not None:
            good_bad_all.writerow({"name": row["Art URL"], "tags": good})

print(brvtal_total, "brvtal /", not_brvtal_total, "not brvtal /", both_total, "both /", neither_total, "neither")
print(black_total, "black /", death_total, "death")
print(good_total, "good /", bad_total, "bad")
print(good_all_total, "good /", bad_all_total, "bad")
