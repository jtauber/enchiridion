Enchiridion
===========

Epictetus's Enchiridion text and analysis

`orig/` directory contains various English and Greek versions of the text.

`analysis/enchiridion.txt` was produced by running `scripts/initial-convert.py` on
`orig/GK_schenkl.txt`.

`scripts/tokens-to-parts.py` converts the text in `analysis/enchiridion.txt` to a line-per-verse format which can be found in `text/enchiridion.txt`.

`text/` also contains the English translations manually formatted in the same format as the top level `enchiridion.txt` file.

`analysis/tagged.tsv` contains a tagged Enchiridion text initially achieved by aligning `text/enchiridion.txt` with the analysis in the Diorisis corpus (with some corrections to the text). It is now being manually corrected and disambiguated in `analysis/glossing.txt`.

`analysis/tagged_glossed.tsv` contains the same tagging but with glosses as well (initially from Perseus/Logeion shortdefs). It is also being manually corrected and disambiguated.

A static website is being generated in `docs/` and served up at <https://jtauber.github.io/enchiridion>.
