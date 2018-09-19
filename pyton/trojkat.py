#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  trojkat.py


def trojkat(a, b, c):
    """"
    Funkcja przyjmuje 3 liczby - długości boków trójkąta
    Funkcja sprawdza czy da się z nich zbudować trójkąt
    Funckja zwraca True luib Folse
    """

    wynik = False

    if a + b > c and b + c > a and a + c > b:
        wynik = True

    return wynik


def main(args):
    assert(trojkat(3, 5, 7) == True)
    assert(trojkat(3, 5, 9) == False)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
