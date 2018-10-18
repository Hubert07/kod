#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cwc_petle.py


def main(args):
    a = 0
    b = 0
    while b <= 75:
        a = int(input("Pierwsza liczba: "))
        b = a + b
        print("Wynik:", b)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
