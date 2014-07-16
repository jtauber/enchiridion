#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml

with open("lemmatization.yaml") as f:
    lemmatization = yaml.load(f)

good_count_1 = 0
total_count_1 = 0
good_count_all = 0
total_count_all = 0
lemmas_1 = set()
lemmas_all = set()
for line in open("analysis/enchiridion.txt"):
    word_id, text, word, form = line.strip().split()
    chapter = int(word_id.split(".")[0])
    if chapter == 24:
        if form.decode("utf-8") not in lemmatization:
            print line
        if lemmatization[form.decode("utf-8")] is not None:
            good_count_1 += 1
            for entry in lemmatization[form.decode("utf-8")]:
                lemmas_1.add(entry["lemma"])
        else:
            print form
        total_count_1 += 1
    else:
        if lemmatization[form.decode("utf-8")] is not None:
            good_count_all += 1
            for entry in lemmatization[form.decode("utf-8")]:
                lemmas_all.add(entry["lemma"])
        total_count_all += 1

print "%d/%d = %0.2f%% [%d lemmas]" % (good_count_1, total_count_1, 100. * good_count_1 / total_count_1, len(lemmas_1))
print "%d/%d = %0.2f%% [%d lemmas]" % (good_count_all, total_count_all, 100. * good_count_all / total_count_all, len(lemmas_all))
