#! /usr/bin/env python
# -*- coding: utf-8 -*-


def main(args):
    a = int(input("Podaj wysokość choinki: "))
    c = str(input("Podaj znak, którym ma być rysowana choinka: "))

    for x in range(0, a, 1):
        print((a - x) * c)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
