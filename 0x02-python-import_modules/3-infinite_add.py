#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    addition = 0
    for args in sys.argv[1:]:
        addition += int(args)
    print(addition)
