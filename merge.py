#!/usr/bin/env python3

import unicodedata

def nfc(token):
    return unicodedata.normalize("NFC", token)


def convert(analyses, pos):
    if pos in ["-"]:
        return analyses
    elif pos in [
        "article", "pronoun", "noun", "adjective", "proper", "adverb@case", "verb@adj"
    ]:
        a = []
        for analysis in analyses.split("|"):
            gender = "-"
            number = "-"
            case = "-"
            other = ""
            for component in analysis.split(" "):
                if component in [
                    "fem", "masc", "neut", "masc/neut", "masc/fem", "masc/fem/neut",
                    "nom", "voc", "acc", "gen", "dat", "nom/voc", "nom/voc/acc", "nom/acc",
                    "sg", "dual", "pl",
                    "1st", "2nd",
                               "(attic",  "(doric",  "(epic",
                                           "doric",   "epic",  "homeric",  "ionic",
                    "aeolic)",             "doric)",  "epic)",             "ionic)",
                               "(attic)", "(doric)", "(epic)",            "(ionic)",
                    "comp", "superl",
                    "adverbial",
                ]:
                    if component == "fem":
                        gender = "F"
                    elif component == "masc":
                        gender = "M"
                    elif component == "neut":
                        gender = "N"
                    elif component == "masc/neut":
                        gender = "Y"
                    elif component == "masc/fem":
                        gender = "Z"
                    elif component == "masc/fem/neut":
                        gender = "X"
                    elif component == "nom":
                        case = "N"
                    elif component == "voc":
                        case = "V"
                    elif component == "acc":
                        case = "A"
                    elif component == "gen":
                        case = "G"
                    elif component == "dat":
                        case = "D"
                    elif component == "nom/voc":
                        case = "N"
                    elif component == "nom/voc/acc":
                        case = "S"
                    elif component == "nom/acc":
                        case = "S"
                    elif component == "sg":
                        number = "S"
                    elif component == "dual":
                        number = "D"
                    elif component == "pl":
                        number = "P"
                    elif component == "1st":
                        other += "1"
                    elif component == "2nd":
                        other += "2"
                    elif component == "comp":
                        other += "C"
                    elif component == "superl":
                        other += "S"
                else:
                    print("@@@", component)
                    quit()
            a.append(case+number+gender+other)
        return "^".join(a)

    elif pos in ["verb"]:
        a = []
        for analysis in analyses.split("|"):
            mood = "-"
            tense = "-"
            voice = "-"
            person = "-"
            number = "-"
            case = "-"
            gender = "-"
            for component in analysis.split(" "):
                if component in [
                    "ind", "inf", "subj", "opt", "imperat", "part",
                    "pres", "imperf", "fut", "aor", "perf", "plup", "futperf",
                    "act", "mid", "mp", "pass",
                    "fem", "masc", "neut", "masc/neut", "masc/fem", "masc/fem/neut",
                    "nom", "voc", "acc", "gen", "dat", "nom/voc", "nom/voc/acc", "nom/acc",
                    "sg", "dual", "pl",
                    "1st", "2nd", "3rd",
                    ""
                               "(attic",  "(doric",  "(epic", "(homeric",
                                           "doric",   "epic",  "homeric",  "ionic",
                    "aeolic)",             "doric)",  "epic)",             "ionic)",
                               "(attic)", "(doric)", "(epic)",            "(ionic)",
                ]:
                    if component == "ind":
                        mood = "I"
                    elif component == "inf":
                        mood = "N"
                    elif component == "subj":
                        mood = "S"
                    elif component == "opt":
                        mood = "O"
                    elif component == "imperat":
                        mood = "D"
                    elif component == "part":
                        mood = "P"
                    elif component == "pres":
                        tense = "P"
                    elif component == "imperf":
                        tense = "I"
                    elif component == "fut":
                        tense = "F"
                    elif component == "aor":
                        tense = "A"
                    elif component == "perf":
                        tense = "X"
                    elif component == "plup":
                        tense = "Y"
                    elif component == "futperf":
                        tense = "Z"
                    elif component == "act":
                        voice = "A"
                    elif component == "mid":
                        voice = "M"
                    elif component == "mp":
                        voice = "M"
                    elif component == "pass":
                        voice = "P"
                    elif component == "nom":
                        case = "N"
                    elif component == "voc":
                        case = "V"
                    elif component == "acc":
                        case = "A"
                    elif component == "gen":
                        case = "G"
                    elif component == "dat":
                        case = "D"
                    elif component == "nom/voc":
                        case = "N"
                    elif component == "nom/voc/acc":
                        case = "S"
                    elif component == "nom/acc":
                        case = "S"
                    elif component == "sg":
                        number = "S"
                    elif component == "dual":
                        number = "D"
                    elif component == "pl":
                        number = "P"
                    elif component == "1st":
                        person = "1"
                    elif component == "2nd":
                        person = "2"
                    elif component == "3rd":
                        person = "3"
                else:
                    print("@@@", component)
                    quit()
            if mood in "DISO":
                a.append(tense + voice + mood + "." + person + number)
                assert case == "-"
                assert gender == "-"
            elif mood in "N":
                a.append(tense + voice + mood)
                assert case == "-"
                assert gender == "-"
                assert person == "-"
                assert number == "-"
            elif mood in "P":
                a.append(tense + voice + mood + "." + case + number + gender)
                assert person == "-"
        return "^".join(a)

    elif pos in ["adjective@@@"]:
        return analyses

    elif pos in [
        "particle", "preposition", "adverb", "conjunction", "interjection",
        "adjective@indecl",
    ]:
        if analyses in [
            "indeclform (particle)",
            "indeclform (prep)",
            "indeclform (conj)",
            "indeclform (adverb)",
            "proclitic indeclform (adverb)",
            "adverbial (attic epic doric)",
            "enclitic indeclform (particle)",
            "indeclform (prep)|poetic indeclform (prep)",
            "proclitic indeclform (prep)",
            "proclitic indeclform (conj)",
            "indeclform (adverb)|indeclform (conj)",
            "indeclform (adverb)|indeclform (conj)|indeclform (prep)",
            "indeclform (prep)|epic (poetic indeclform prep)",
            "attic (indeclform adverb)",
            "adverbial",
            "indeclform (interrog)",
            "attic epic (proclitic indeclform adverb)",
            "indeclform (exclam)",
            "enclitic indeclform (adverb)",
            "proclitic poetic indeclform (prep)",
            "aeolic (enclitic indeclform particle)|enclitic indeclform (particle)",
            "contr indeclform (conj)",
            "indeclform (indecl)",
            "indeclform (numeral)",
        ]:
            return "-"
        else:
            print("@@@", analyses)
            quit()
    else:
        print("@@@", pos)
        quit()

with open("analysis/enchiridion-parsing.txt") as f, open("analysis/enchiridion-aligned.txt") as g:
    line = 0
    for a, b in zip(f, g):
        line += 1
        if a.strip() and b.strip():
            a_token = nfc(a.split("\t")[5])
            b_token = nfc(b.split()[2])
            if a_token != b_token:
                print(line)
                print(a)
                print(b)
                print("@@@")
                quit()

        if b.strip():
            ref, text, word, norm = b.strip().split()
        else:
            ref, text, word, norm = None, None, None, None

        if a.strip():
            parts = a.strip().split("\t")
            sentence_id = parts[3]
            word_id = parts[4]
            lemma = parts[6]
            pos = parts[7]
            analyses = parts[10]
            if lemma == "None":
                lemma = "-"
            if pos == "None":
                pos = "-"
            if analyses == "None":
                analyses = "-"
        else:
            sentence_id, word_id, lemma, pos, analyses = "-", "-", "-", "-", "-"

        if ref:
            if word_id != "-":
                assert int(word_id) < 100
                word_id = f"{int(sentence_id):03d}.{int(word_id):02d}"
            else:
                word_id = "-"
            print(ref, word_id, text, word, norm, lemma, pos, convert(analyses, pos), sep="\t")
