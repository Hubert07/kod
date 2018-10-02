#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cwc_petle2.py
#  


def main(args):
    start = int(input("Pierwsza liczba: "))
    stop = int(input("Druga liczba: "))
   
    if start < stop:
        for liczba in range(start, stop + 1):
                print(liczba, " ")
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
