#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv) - 1
    msg = "arguments"
    if i == 1:
        print("{} {}:".format(i, msg[:8]))
    else:
        print("{} {}{}".format(i, msg,
              "." if i == 0 else ":"))
    for ac, name in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(ac, name))
