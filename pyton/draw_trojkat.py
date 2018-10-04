#! /usr/bin/env python
# -*- coding: utf-8 -*-


def main(args):
    a = int(input("Podaj wysokość trójkata: "))
    c = str("*")

    for x in range(1, a, 1):
        b = x + (x - 1)
        if x == 1:
            print("", b * c, "")
        else:
            print(b * c)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
