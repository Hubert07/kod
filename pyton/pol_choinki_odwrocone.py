#! /usr/bin/env python
# -*- coding: utf-8 -*-


def main(args):
    a = int(input("Podaj wysokość choinki: "))
    c = str(input("Podaj znak, którym ma być rysowana choinka: "))

    for a in range(a, 1, a - 1):
        print(a * c)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
