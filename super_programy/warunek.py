#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wej-wyj.py
#
#


def main(args):
    a = int(input("Podaj 1 liczbe: "))
    b = int(input("Podaj 2 liczbe: "))
    c = int(input("Podaj 3 liczbe: "))

    if a > b:
        if a > c:
            print("Największa liczba to ", a)

    if b > a:
        if b > c:
            print("Największa liczba to ", b)

    if c > a:
        if c > b:
            print("Największa liczba to ", c)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
