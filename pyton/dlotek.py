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
    i = 0
# for i in range(ileliczb):
    while i < ileliczb:
        liczba = random.randint(1, maksliczba + 1)
        if liczby.count(liczba) == 0:  # sprawdzenie czy liczba już jest
            liczby.append(liczba)
            i += 1  # powiększ i o 1
    print(liczby)

    typy = set()  # dekPlarowanie pustego zbioru na typy użytkownika
    i = 0
    while i < ileliczb:
        typ = input("Podaj liczbę {}:".format(i + 1))
        if typ not in typy:  # jeżeli podanego typu nei ma w zbiorze
            typy.add(typ)  # dodaj typ uzytkownika
            i += 1  # dodaj do zbioru
    print(typy)

    if typy ==

    # if liczba == int(odp):
    #     print('Umiesz w liczby')
    #     break  # przerwanie działania pętli
    # else:
    #      print('No chyba nie')

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
