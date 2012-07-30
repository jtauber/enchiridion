#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

SINGLE_LETTER = "(" + "|".join([
    "γ", "μ", "σ",
]) + ")"

INITIAL_CONSONANT_CLUSTER = "(" + "|".join([
    "β", "γ", "δ", "ζ", "θ", "κ", "λ", "μ", "ν", "π", "ρ", "σ", "τ", "φ", "χ",
    "ψ", "βλ", "βρ", "γλ", "γν", "γρ", "δρ", "θλ", "θρ", "κλ", "κρ", "κτ",
    "μν", "πλ", "πρ", "πτ", "σκ", "σμ", "σπ", "στ", "σφ", "σχ", "τρ", "φθ",
    "φρ", "χρ", "στρ",
    "Ζ",
]) + ")"

INITIAL_VOWEL = "(" + "|".join([
    "ἅ", "ἄ",
    "ἐ", "ἔ", "ἕ", "ἕ",
    "ἡ", "ἤ", "ᾖ", "ᾖ", "ἡ", "ἥ", "ἦ",
    "ὁ", "ὁ", "ὅ",
    "ὦ", "ᾧ", "ὡ", "ὤ", "ὧ",
    "αἱ",
    "εἰ", "εἶ",
    "οἱ", "οὐ", "οὔ", "οὗ",
]) + ")"

MIDDLE_VOWEL = "(" + "|".join([
    "ά",
    "ε", "έ",
    "ή", "ῇ",
    "ι", "ί",
    "ό",
    "ύ",
    "ῷ",
    "εῦ",
]) + ")"

FINAL_CONSONANT = "(" + "|".join([
    "κ",
    "ν",
    "ς",
    "τ",
]) + ")"

SINGLE_SYLLABLE = "(" + \
    "(" + SINGLE_LETTER + ")" + \
    "|" + \
    "(" + INITIAL_CONSONANT_CLUSTER + MIDDLE_VOWEL + ")" + \
    "|" + \
    "(" + INITIAL_VOWEL + ")" + \
    "|" + \
    "(" + INITIAL_VOWEL + FINAL_CONSONANT + ")" + \
")"

INITIAL_SYLLABLE = "(" + \
    "(" + INITIAL_CONSONANT_CLUSTER + MIDDLE_VOWEL + ")" + \
    "|" + \
    "(" + INITIAL_VOWEL + ")" + \
")"

MIDDLE_SYLLABLE = "(" + \
    "(" + INITIAL_CONSONANT_CLUSTER + MIDDLE_VOWEL + ")" + \
    "|" + \
    "(" + MIDDLE_VOWEL + ")" + \
")"

FINAL_SYLLABLE = "(" + \
    "(" + INITIAL_CONSONANT_CLUSTER + MIDDLE_VOWEL + ")" + \
    "|" + \
    "(" + MIDDLE_VOWEL + ")" + \
")"

MULTI_SYLLABLE = "(" + \
    "(" + INITIAL_SYLLABLE + ")" + \
    "(" + MIDDLE_SYLLABLE + ")*" + \
    "(" + FINAL_SYLLABLE + ")" + \
")"

pattern = "^" + SINGLE_SYLLABLE + "|" + MULTI_SYLLABLE + "$"

for line in open("analysis/enchiridion.txt"):
    word = line.strip().split()[2].strip("@")
    if not re.match(pattern, word):
        print word
        break
