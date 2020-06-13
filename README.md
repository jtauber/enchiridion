# Enchiridion

Epictetus's Enchiridion text and analysis

This text is being prepared as part of the [Greek Learner Texts Project](https://greek-learner-texts.org/).

`orig/` directory contains various English and Greek versions of the text.

`analysis/enchiridion.txt` was produced by running `scripts/initial-convert.py` on
`orig/GK_schenkl.txt`.

`scripts/tokens-to-parts.py` converts the text in `analysis/enchiridion.txt` to a line-per-verse format which can be found in `text/enchiridion.txt`.

`text/` also contains the English translations manually formatted in the same format as the `enchiridion.txt` file.

`analysis/tagged.tsv` contains a tagged Enchiridion text initially achieved by aligning `text/enchiridion.txt` with the analysis in the Diorisis corpus (with some corrections to the text). It is now being manually corrected and disambiguated in `analysis/glossing.txt`.

`analysis/tagged_glossed.tsv` contains the same tagging but with glosses as well (initially from Perseus/Logeion shortdefs). It is also being manually corrected and disambiguated.

A static website is being generated in `docs/` and served up at <https://jtauber.github.io/enchiridion>.

## Contributors

* James Tauber

## Source

* The Greek text and Higginson and Long translations come from the Perseus Digital Library.
* The Carter translation comes from http://classics.mit.edu/Epictetus/epicench.html
* The Matheson translation comes from https://www.sacred-texts.com/cla/dep/dep102.htm
* The initial lemmatisation and tagging comes from the Diorisis Ancient Greek Corpus
* The initial glosses come from Logeion

## Progress

The text preparation is complete.

Translation alignment, glossing, and lemma correction has been done up to chapter 13.

## License

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
