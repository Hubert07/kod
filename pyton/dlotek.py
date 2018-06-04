#!/usr/bin/env python
# -*- coding: utf-8 -*-
# def = function i wszystko musi być równe odstępy

import random


def main(args):
    ileliczb = int(input('Podaj ilość typowanych liczb:'))
    maksliczba = int(input('Podaj maks. losowaną liczbę:'))
    print('wytypuj {} z {} liczb'.format(ileliczb, maksliczba))

# losowanie
    liczby = []  # lista wylosowanych liczb
    for i in range(ileliczb):
        liczba = random.randint(1, maksliczba)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
    print(liczby)

    # if liczba == int(odp):
    #     print('Umiesz w liczby')
    #     break  # przerwanie działania pętli
    # else:
    #      print('No chyba nie')

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
