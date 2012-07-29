# -*- coding: utf-8 -*-

import unicodedata

VARIA = u"\u0300"
OXIA = u"\u0301"
PSILI = u"\u0313"
DASIA = u"\u0314"
PERISPOMENI = u"\u0342"

ACCENTS = [VARIA, OXIA, PERISPOMENI]


def d(s):
    return unicodedata.normalize("NFD", s)


def strip_accents(s):
   return ''.join((c for c in d(s) if unicodedata.category(c) != "Mn"))


def count_accents(s):
    count = 0
    for c in d(s):
        if c in ACCENTS:
            count += 1

def n(x):
    return unicodedata.normalize("NFKC", x)


def strip_last_accent(word):
    x = list(word)
    for i, ch in enumerate(x[::-1]):
        s = strip_accents(ch)
        if s != ch:
            x[-i - 1] = s
            break
    return u"".join(x)


ELISION = [
    u"ἀλλά",
    u"ἀντί",
    u"ἀπό",
    u"δέ",
    u"διά",
    u"ἐπί",
    u"κατά",
    u"μετά",
    u"οὐδέ",
    u"μηδέ",
    u"παρά",
    u"τοῦτο",
    u"ταῦτα",
    u"ὑπό",
]


elision_dict = {}
for word in ELISION:
    elided = d(word[:-1]) + u" \u0313"
    elision_dict[elided] = word
    if elided[-3] == u"τ":
        elision_dict[elided[:-3] + u"θ \u0313"] = word
    elif elided[-3] == u"π":
        elision_dict[elided[:-3] + u"φ \u0313"] = word

# for k, v in elision_dict.items():
#     print k, v

CLITICS = [
    u"εἰμί",
    u"εἰσίν",
    u"ἐσμέν",
    u"ἐστέ",
    u"γέ",
    u"ποτέ",
    u"τέ",
    u"φησίν",
    u"πώς",
    u"ποῦ",
    u"φημί",
]

clitics_dict = {}
for word in CLITICS:
    clitics_dict[strip_last_accent(word)] = word


def convert(word):
    # print "converting", word
    norm = word.decode("utf-8")
    
    # change graves to acutes
    temp = u""
    for ch in d(norm):
        if ch == VARIA:
            ch = OXIA # OXIA will be normalized to TONOS below if needed
        temp += ch
    norm = n(temp)
    
    if count_accents(norm) == 2:
        norm = strip_last_accent(norm)
        assert count_accents(norm) == 1
    
    # # normalize movable nu in 3rd person verb
    # if norm.endswith(u"εν"):
    #     norm = norm[:-1] + u"(ν)@"
    # if norm.endswith(u"ε"):
    #     norm = norm + u"(ν)@"
    
    if count_accents(norm) == 0:
        if norm in clitics_dict:
            norm = clitics_dict[norm]
    
    # if (
    #     norm.endswith(u"σιν") or
    #     norm.endswith(u"σίν") or
    #     norm.endswith(u"ξίν") or
    #     norm.endswith(u"ξιν")
    # ):
    #     norm = norm[:-1] + u"(ν)@"
    # if (
    #     norm.endswith(u"σι") or
    #     norm.endswith(u"σί") or
    #     norm.endswith(u"ξί")
    # ):
    #     norm = norm + u"(ν)@"
    
    # if norm in [u"ἐστιν", u"ἐστίν", u"ἐστι", u"ἐστί", u"ἔστιν", u"ἔστι"]: # @@@
    #     norm = u"ἐστί(ν)"
    
    # if norm in [u"ἔξεστιν", u"ἔξεστι"]:
    #     norm = u"ἔξεστι(ν)"
    
    # if norm == u"πάρεστιν":
    #     norm = u"πάρεστι(ν)"
    
    if norm == u"ἐξ":
        norm = u"ἐκ@"
    
    if norm in [u"οὐκ", u"οὐχ"]:
        norm = u"οὐ"
    
    if norm in [u"μέχρι", u"μέχρις"]:
        norm = u"μέχρι(ς)"
    
    if norm in [u"οὕτω", u"οὕτως"]:
        norm = u"οὕτω(ς)"
    
    # elision
    if norm.endswith(u" \u0313"):
        if d(norm) in elision_dict:
            norm = elision_dict[d(norm)]
    
    # proclitics
    if norm == u"εἴ":
        norm = u"εἰ@"
    elif norm == u"εἴς":
        norm = u"εἰς@"
    elif norm == u"ἔν":
        norm = u"ἐν@"
    elif norm == u"ὅ":
        norm = u"ὁ@"
    elif norm == u"ὥς":
        norm = u"ὡς@"
    
    return norm.encode("utf-8")
