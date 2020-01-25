#!/usr/bin/env python3

from roman_numerals import convert_to_numeral


def output(src, dest, title, subtitle, lang):
    HEADER = f"""\
<!DOCTYPE html>
<html lang="{lang}">
<head>
<title>{title}</title>
<meta charset="utf-8">
<link href="https://fonts.googleapis.com/css?family=Noto+Serif:400,700&amp;subset=greek,greek-ext" rel="stylesheet">
<link href="style.css" rel="stylesheet">
</head>
<body>
  <div class="container">
    <nav>&#x2191; <a href="./">Open Epictetus</a></nav>
    <h1 class="title" lang="en">{title}</h1>
    <h2 class="subtitle" lang="en">{subtitle}</h1>
"""

    FOOTER = """\
  </div>
</body>
</html>
"""

    with open(src) as f:
        with open(dest, "w") as g:
            prev_chapter = None
            print(HEADER, file=g)
            for line in f:
                parts = line.strip().split(maxsplit=1)
                chapter, verse = parts[0].split(".")
                if prev_chapter != chapter:
                    if prev_chapter is not None:
                        print("""    </div>""", file=g)
                    if chapter == "0":
                        print("""    <div class="preamble">""", file=g)
                    else:
                        if chapter == "SB":
                            print("""    <div class="subscription">""", file=g)
                        elif chapter == "EP":
                            print("""    <div class="epilogue">""", file=g)
                        else:
                            print("""    <div class="chapter">""", file=g)
                            print(f"""      <h3 class="chapter_ref">{convert_to_numeral(int(chapter))}</h3>""", file=g)
                    prev_chapter = chapter
                if chapter == "0" and verse == "0":
                    print(f"""    <h2 class="section_title">{parts[1]}</h2>""", file=g)
                else:
                    if chapter == "EP" and verse == "0":
                        print(f"""<h3 class="epilogue_title">{parts[1]}</h3>""", file=g)
                    else:
                        if verse != "1":
                            print(f"""      <span class="verse_ref">{verse}</span>""", end="&nbsp;", file=g)
                        print(parts[1], file=g)
            print("""    </div>""", file=g)
            print(FOOTER, file=g)


output("enchiridion.txt", "docs/GK_schenkl.html", "The Enchiridion of Epictetus", "Greek Edition of Schenkl", "grc")
output("formatted/EN_carter.txt", "docs/EN_carter.html", "The Enchiridion of Epictetus", "English Translation by Carter", "en")
output("formatted/EN_higginson.txt", "docs/EN_higginson.html", "The Enchiridion of Epictetus", "English Translation by Higginson", "en")
output("formatted/EN_long.txt", "docs/EN_long.html", "The Enchiridion of Epictetus", "English Translation by Long", "en")
output("formatted/EN_matheson.txt", "docs/EN_matheson.html", "The Enchiridion of Epictetus", "English Translation by Matheson", "en")
