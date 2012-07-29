#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys
import normalise

def is_greek(word):
    word = word.decode("utf-8")
    for ch in word:
        if 0x301 <= ord(ch) < 0x3FF:
            pass
        elif 0x1F00 <= ord(ch) <= 0x1FF7:
            pass
        elif ch in [".", ",", ":", "(", ")", ";", "\"", "[", "]"]:
            pass
        elif ord(ch) in [0x2019, 0x2018]:
            pass
        else:
            return False
    return True
    

def chapter_milestone(word):
    if word[-1] != ".":
        return False
    try:
        convert_chapter_milestone(word)
        return True
    except ValueError:
        return False
    

def convert_chapter_milestone(word):
    return int(word[:-1])


def verse_milestone(word):
    if word[0] != "[" or word[-1] != "]":
        return False
    try:
        convert_verse_milestone(word)
        return True
    except ValueError:
        return False
    

def convert_verse_milestone(word):
    return int(word[1:-1])


def strip_punctuation(x):
    y = x.decode("utf-8")
    y = re.sub(u"^[‘\[\(⸂⸄⸀⸁—⟦12]+", "", y)
    y = re.sub(u"[\]\.,:;\)·⸃⸅;—⸂⟧’]+$", "", y)
    return y.encode("utf-8")


chapter = 0
verse = 1
entry = 1

for line in file(sys.argv[1]):
    for word in line.strip().split():
        if is_greek(word):
            word_punc_stripped = strip_punctuation(word)
            print "%02d.%02d.%03d %s %s %s" % (chapter, verse, entry, word, word_punc_stripped, normalise.convert(word_punc_stripped))
            entry += 1
        elif chapter_milestone(word):
            chapter = convert_chapter_milestone(word)
            verse = 1
            entry = 1
        elif verse_milestone(word):
            verse = convert_verse_milestone(word)
            entry = 1
        else:
            print word
            assert False
