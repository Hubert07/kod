#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random


def main(args):
    x = int(input("Podaj rozmiar tablicy: "))
    if x > 25:
        print("Tablica nie może być większa niż 25")
        x = int(input("Podaj rozmiar tablicy: "))
    zakres = 50
    liczby = []
    i = 0

    while i < x:
        los = random.randint(1, zakres + 1)
        if liczby.count(los) == 0:
            liczby.append(los)
            i += 1
    print(liczby)

    traf = int(input("Wytypuj liczbę od 0 do 50: "))

    for j in range(0, x, 1):
        brawo = 0
        if liczby[j] == traf:
            brawo = 1
        else:
            brawo = 0
    if brawo == 1:
        print("Brawo, wytypowałeś jedną z wylosowanych liczb")
    elif brawo == 0:
        print("Przykro mi, ale nie udało Ci się wytypować poprawnej liczby")

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
