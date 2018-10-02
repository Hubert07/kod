#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  suma_cyfr_v2.py
#
# DANE WEJŚCIOWE liczba l2 dwucyfrowa podawana przez użytkownika
# DANE WYJŚCIOWE suma cyfr podanych przez użytkownika
# jupyter qtconsole


def suma_cyfr(l2):
    suma = 0

    for cyfra in l2:
        suma += cyfra
    # while l2 > 0:
    #     suma += l2 % 10
    #     l2 = int(l2 / 10)

    return suma


def main(args):
    assert(suma_cyfr("111") == 3)
    assert(suma_cyfr("786") == 21)
    assert(suma_cyfr("924") == 15)

    # l2 = int(input("Podaj liczbę: "))
    # while l2 < 10:
    #    l2 = int(input("Podaj liczbę: "))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
