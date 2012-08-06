#!/usr/bin/env python3

import unicodedata


def breakdown(ch):
    b = {}
    for component in unicodedata.normalize("NFD", ch):
        if 0x391 <= ord(component) <= 0x3A9:
            b["base"] = component
        elif 0x3B1 <= ord(component) <= 0x3C9:
            b["base"] = component
        elif ord(component) == 0x300:  # grave / varia
            b["accent"] = "grave"
        elif ord(component) == 0x301:  # acute / oxia
            b["accent"] = "acute"
        elif ord(component) == 0x308:  # diaeresis / dialytika
            b["division"] = "diaresis"
        elif ord(component) == 0x313:  # smooth / psili
            b["breathing"] = "smooth"
        elif ord(component) == 0x314:  # rough / dasia
            b["breathing"] = "rough"
        elif ord(component) == 0x342:  # circumflex / perispomeni
            b["accent"] = "circumflex"
        elif ord(component) == 0x345:  # iota subscript / ypogegrammeni
            b["subscript"] = "iota"
        elif ord(component) == 0x1FBD:  # apostrophe; should be U+2019?
            b["punctuation"] = "apostrophe"
        else:
            print(ch, ":\t", component, hex(ord(component)))
            quit()
    return b
        
for line in open("analysis/enchiridion.txt"):
    word = line.strip().split()[2].strip("@")
    for ch in word:
        print(ch, breakdown(ch))
