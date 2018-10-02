#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  suma_cyfr.py
#
# DANE WEJŚCIOWE liczba l2 dwucyfrowa podawana przez użytkownika
# DANE WYJŚCIOWE suma cyfr podanych przez użytkownika
# jupyter qtconsole


def suma_cyfr(l2):
    suma = 0
    while l2 > 0:
        suma += l2 % 10
        l2 = int(l2 / 10)
    print("Suma cyfr: ", suma)
    return suma


def main(args):

    assert(suma_cyfr(111) == 3)
    assert(suma_cyfr(4568) == 23)
    assert(suma_cyfr(9996) == 33)
    assert(suma_cyfr(846) == 18)

    # l2 = int(input("Podaj liczbę: "))
    # while l2 < 10:
    #    l2 = int(input("Podaj liczbę: "))

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
