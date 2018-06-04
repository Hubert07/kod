#!/usr/bin/env python
# -*- coding: utf-8 -*-
# kodowanie ^
# def = function i wszystko musi być równe odstępy

import random


def main(args):
        liczba = random.randint(1, 10)
        # print('Los wybrał Ci:', liczba)
        for i in range(3):
            odp = input('Podaj liczbę od 1 do 10:')
            print('Wybrałeś liczbę:', odp)

            if liczba == int(odp):
                print('Umiesz w liczby')
                break  # przerwanie działania pętli
            else:
                print('No chyba nie')

            return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
