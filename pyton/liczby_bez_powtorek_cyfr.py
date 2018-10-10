#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tabliczka_mnozenia.py
#
#  Copyright 2018  <>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  pyformat.com dobra  strona


def liczby2(a, b):
    """
    Drukuje wszystki liczby dwucydrowe, którym nie powatarzają się cyfry
    np.: 11, 22, 33 ...
    Oraz zwraca ich ilość
    """

    d = 0

    for x in range(a, b + 1, 1):
        if x % 11 != 0:
            d = d + 1
            print(x)
    print("Ilośc takich liczb: ", d)

    return ""


def suma_cyfr(x):
    suma = 0
    while x > 1:
        suma += x % 10
        x = int(x / 10)

    return suma


def liczby3(a, b):
    """
    Drukuje wszystkie liczby 3 cyfrowe, gdzie nie powtarzają się cyfry
    Bez 111 112 11x, 66x itd
    """

    ilosc = 0

    for i in range(1, 10):
        for j in range(0, 10):
            if i != j:
                for k in range(0, 10):
                    if i != k and j != k:
                        z = 100 * i + 10 * j + k
                        print(z)
                        ilosc = ilosc + 1
    print("Ilośc takich liczb: ", ilosc)

    return "To była funkcja Liczby3"

    # for x in range(a, b + 1, 1):
    #     c = x % 111
    #     d = x % 110
    #     e = x % 101
    #     g = x % 100
    #     z = x % 10
    #     f = (x - z) % 11
    #     h = (x % 100)
    #     if c != 0 and d != 0 and e != 0 and g != 0 and f != 0:
    #         print(x)


def main(args):

    print(liczby2(10, 99))
    print(liczby3(100, 999))

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
