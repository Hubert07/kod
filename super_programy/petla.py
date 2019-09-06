#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wej-wyj.py
#
#
import random


def main(args):
    ileliczb = 5
    zakres = 30
    for i in range(0, ileliczb, 1):
        liczba = random.randint(1, zakres)
        print(liczba)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
