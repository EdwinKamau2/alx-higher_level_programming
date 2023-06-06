#!/usr/bin/python3
def uppercase(str):
    for alph in str:
        alph = ord(alph)
        if 96 < alph < 123:
            alph -= 32
        print("{}".format(chr(alph)), end="")
    print()
