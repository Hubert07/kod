#! /usr/bin/env python
# -*- coding: utf-8 -*-


def main(args):
    a = int(input("Podaj długośc pierwszego boku: "))
    b = int(input("Podaj długośc drugiego boku: "))
    c = str(input("Podaj znak, którym ma być rysowany prostokąt: "))
    d = b - 4

    for x in range(1, a + 1, 1):
        if x > 1 and x < a:
            print(c, d * " ", c)
        else:
            print(b * c)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
