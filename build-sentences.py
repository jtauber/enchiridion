#!/usr/bin/env python3

import collections


sentence_ids = []
tokens = collections.defaultdict(list)
translation_A = {}
translation_B = {}
translation_C = {}
translation_D = {}

with open("glossing.txt") as f:
    for line in f:
        line = line.strip()
        if line == "":
            pass
        elif line.startswith("# "):
            current_sentence = line[2:]
            sentence_ids.append(current_sentence)
        elif line[0].isdigit():
            ref, sent_word, text, word, norm, lemma, pos, analysis, gloss = line.split("\t")
            assert sent_word.startswith(current_sentence)
            tokens[current_sentence].append((ref, text, lemma, pos, analysis, gloss))
        elif line[0] in "ABCD":
            if line.startswith("A. "):
                translation_A[current_sentence] = line[3:]
            if line.startswith("B. "):
                translation_B[current_sentence] = line[3:]
            if line.startswith("C. "):
                translation_C[current_sentence] = line[3:]
            if line.startswith("D. "):
                translation_D[current_sentence] = line[3:]
        else:
            print(line)
            print("@@@")
            quit()


def trigrams(it):

    prev_2 = None
    prev_1 = None

    for current in it:
        if prev_1 is not None:
            yield prev_2, prev_1, current

        prev_2 = prev_1
        prev_1 = current

    yield prev_2, prev_1, None


def print_pagination(prev, next, g):
    print("""    <div class="pagination">""", file=g)
    if prev:
        print(f"""      <a href="./{prev}.html">&laquo; {prev}</a>""", file=g)
    else:
        print("""      <span>&nbsp;</span>""", file=g)
    if next:
        print(f"""      <a href="./{next}.html">{next} &raquo;</a>""", file=g)
    else:
        print("""      <span>&nbsp;</span>""", file=g)
    print("""    </div>""", file=g)


for prev, sentence_id, next in trigrams(sentence_ids):

    dest = f"docs/sentences/{sentence_id}.html"

    title = f"Echiridion"
    subtitle = f"Sentence {sentence_id}"
    HEADER = f"""\
<!DOCTYPE html>
<html">
<head>
<title>{title} [{subtitle}]</title>
<meta charset="utf-8">
<link href="https://fonts.googleapis.com/css?family=Noto+Serif:400,400i,700&amp;subset=greek,greek-ext" rel="stylesheet">
<link href="../style.css" rel="stylesheet">
</head>
<body>
  <div class="wide-container">
    <nav>&#x2191; <a href="../">Open Epictetus</a></nav>
    <h1 class="title" lang="en">{title}</h1>
    <h2 class="subtitle" lang="en">{subtitle}</h1>
"""

    FOOTER = """\
  </div>
</body>
</html>
"""

    with open(dest, "w") as g:
        print(HEADER, file=g)

        print_pagination(prev, next, g)

        print("""    <section class="tokens"><h2>Text and Analysis</h2>""", file=g)
        for token in tokens[sentence_id]:
            ref, text, lemma, pos, analysis, gloss = token
            print("""      <div class="token">""", file=g)
            print(f"""        <div class="ref">{ref}</div>""", file=g)
            print(f"""        <div class="text">{text}</div>""", file=g)
            print(f"""        <div class="lemma">{lemma}</div>""", file=g)
            print(f"""        <div class="pos">{pos}</div>""", file=g)
            print(f"""        <div class="analysis">{analysis}</div>""", file=g)
            print(f"""        <div class="gloss">{gloss}</div>""", file=g)
            print("""      </div>""", file=g)
        print("""      <p class="issues">If you find any errors, please file a <a href="https://github.com/jtauber/enchiridion/issues">GitHub issue</a>.</p>""", file=g)
        print("""    </section>""", file=g)


        print(f"""    <section class="translations"><h2>Translations</h2>""", file=g)
        print(f"""      <div class="translation">{translation_A[sentence_id]}<cite>Elizabeth Carter (c.1750)</cite></div>""", file=g)
        print(f"""      <div class="translation">{translation_B[sentence_id]}<cite>Thomas Wentworth Higginson (1890)</cite></div>""", file=g)
        print(f"""      <div class="translation">{translation_C[sentence_id]}<cite>George Long (1890)</cite></div>""", file=g)
        print(f"""      <div class="translation">{translation_D[sentence_id]}<cite>Percy Ewing Matheson (1916)</cite></div>""", file=g)
        print(f"""    </section>""", file=g)

        print_pagination(prev, next, g)

        print(FOOTER, file=g)
