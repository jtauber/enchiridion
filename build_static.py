#!/usr/bin/env python3

from roman_numerals import convert_to_numeral


SRC = "enchiridion.txt"
DEST = "docs/index.html"

TITLE = "The Enchiridion of Epictetus"

HEADER = f"""\
<!DOCTYPE html>
<html lang="grc">
<head>
<title>{TITLE}</title>
<meta charset="utf-8">
<link href="https://fonts.googleapis.com/css?family=Noto+Serif:400,700&amp;subset=greek,greek-ext" rel="stylesheet">
<link href="style.css" rel="stylesheet">
</head>
<body>
  <div class="container">
    <h1 lang="en">{TITLE}</h1>
"""
#   <nav>&#x2191; <a href="./">Open Apostolic Fathers</a></nav>
# """

FOOTER = """\
  </div>
</body>
</html>
"""

with open(SRC) as f:
    with open(DEST, "w") as g:
        prev_section = None
        prev_chapter = None
        print(HEADER, file=g)
        for line in f:
            parts = line.strip().split(maxsplit=1)
            ref = parts[0].split(".")
            if len(ref) == 2:
                section = None
                chapter, verse = ref
            else:
                section, chapter, verse = ref
            if prev_section != section:
                if prev_section is not None:
                    print("   </div>""", file=g)
                    print("   </div>""", file=g)
                print("""   <div class="section">""", file=g)
                prev_section = section
                prev_chapter = None
            if prev_chapter != chapter:
                if prev_chapter is not None:
                    if prev_chapter == "0":
                        if section is None:
                            print("""    </div>""", file=g)
                    else:
                        print("""    </div>""", file=g)
                if chapter == "0":
                    if section is None:
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
        if section is not None:
            print("""    </div>""", file=g)
        print(FOOTER, file=g)
