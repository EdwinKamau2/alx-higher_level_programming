#!/usr/bin/python3
for cr in reversed(range(97, 123)):
    print("{:c}".format(cr if (cr % 2 == 0) else (cr - 32)), end='')
