#!/usr/bin/env python3

with open("analysis/enchiridion.txt") as f:
    prev = None
    for line in f:
        ref, text, word, norm = line.strip().split()
        c, v, t = ref.split(".")
        if int(c) == 0:
            continue
        cv = f"{int(c)}.{int(v)}"
        if cv != prev:
            if prev is not None:
                print()
            print(cv, end="")
            prev = cv
        print(f" {text}", end="")
    print()
