#!/usr/bin/env python3

with open("analysis/enchiridion.txt") as f:
    prev = None
    for line in f:
        ref, text, word, norm = line.strip().split()
        c, v, t = ref.split(".")
        cv = f"{c}.{v}"
        if cv != prev:
            if prev is not None:
                print()
            print(cv, end="")
            prev = cv
        print(f" {text}", end="")
    print()
