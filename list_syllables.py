#!/usr/bin/env python3

from syllabify import syllabify, display_syllable

import unicodedata


def d(s):
    return unicodedata.normalize("NFD", s)


def strip_accents(s):
    return ''.join((c for c in d(s) if unicodedata.category(c) != "Mn"))


for line in open("analysis/enchiridion.txt"):
    word = line.strip().split()[2].strip("@")
    for syllable in syllabify(word):
        print(strip_accents(display_syllable(syllable).strip("’").lower()))
