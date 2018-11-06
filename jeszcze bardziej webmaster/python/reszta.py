#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  reszta.py
#


def pobierzNominaly():
    nominaly = set([500, 200, 100, 50, 20, 10, 5, 2, 1])
    n = int(input("Podaj nominial lub 0 aby zakonczyc: "))
    listaNm = []
    while n > 0:
        if n in nominaly:
            listaNm.append(n)
        else:
            print("Niepoprawna wartość")
        n = int(input("Podaj nominial lub 0 aby zakonczyc: "))
    listaNm.sort(reverse=True)  # sortowanie malejące
    return listaNm


def wydajReszte1(r, listaNm):

    i = 0  # indeks nominału
    liczbaNm = len(listaNm)  # liczba nominałów
    while r > 0 and i < liczbaNm:
        while i < liczbaNm and r < listaNm[i]:
            i += 1
        if i < liczbaNm and r >= listaNm[i]:
            nominal = listaNm[i]
            ileNm = int(r / nominal)
            if ileNm > listaNm.count(nominal):
                ileNm = listaNm.count(nominal)
            r -= ileNm * nominal
            for j in range(ileNm):
                listaNm.remove(nominal)
                liczbaNm -= 1
            i = 0
            print("{} x {}".format(ileNm, nominal))
    if r > 0:
        print("Brak nominałów do wydania {}".format(r))


def main(args):

  #listaNm = [200, 100, 20, 10, 5, 2, 1]
    listaNm = pobierzNominaly()
    reszta = int(input("Podaj resztę do wydania: "))
    #wydajReszte1(reszta, listaNm)
    wydajReszte1(reszta, listaNm)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
