#!/usr/bin/env python3

from characters import breakdown


def is_vowel(b):
    return b.get("base") and b["base"].lower() in "αεηιουω"


def is_apostrophe(b):
    return b.get("punctuation") == "apostrophe"


def is_diphthong(b1, b2):
    return b1["base"] + b2["base"] in [
        "αι", "ει", "οι", "υι",
        "αυ", "ευ", "ου", "ηυ",
    ] and b2.get("division") is None


def is_valid_consonant_cluster(b, c):
    s = b["base"].lower() + ("".join(b2.get("base", "") for b2 in c)).lower()
    return s[:2] in [
        "βδ", "βλ", "βρ",
        "γλ", "γν", "γρ",
        "δρ",
        "θλ", "θν", "θρ",
        "κλ", "κν", "κρ", "κτ",
        "μν",
        "πλ", "πν", "πρ", "πτ",
        "σβ", "σθ", "σκ", "σμ", "σπ", "στ", "σφ", "σχ",
        "τρ",
        "φθ", "φλ", "φρ",
        "χλ", "χρ",
    ] or s[:3] in [
        "στρ",
    ]


def display_syllable(s):
    return "".join(b["original"] for b in s)


def display_word(w):
    return ".".join(display_syllable(s) for s in w)


def syllabify(word):
    state = 0
    result = []
    current_syllable = []
    for ch in word[::-1]:
        b = breakdown(ch)
        # print(state, ch, b, display_syllable(current_syllable), display_word(result))
        if state == 0:
            current_syllable.insert(0, b)
            if is_vowel(b):
                state = 1
            elif is_apostrophe(b):
                state = 3
        elif state == 1:
            if is_vowel(b):
                if is_diphthong(b, current_syllable[0]):
                    current_syllable.insert(0, b)
                else:
                    result.insert(0, current_syllable)
                    current_syllable = [b]
            else:
                current_syllable.insert(0, b)
                state = 2
        elif state == 2:
            if is_vowel(b):
                result.insert(0, current_syllable)
                current_syllable = [b]
                state = 1
            else:
                if is_valid_consonant_cluster(b, current_syllable):
                    current_syllable.insert(0, b)
                else:
                    result.insert(0, current_syllable)
                    current_syllable = [b]
                    state = 0
        elif state == 3:
            current_syllable.insert(0, b)
            if is_vowel(b):
                state = 1
    result.insert(0, current_syllable)
    assert state != 0, word
    return result


for line in open("analysis/enchiridion.txt"):
    word = line.strip().split()[2].strip("@")
    print(word, display_word(syllabify(word)))
