#! /usr/bin/env python
# -*- coding: utf-8 -*-


def mnoz(a, b):
    print(a * b)

# zmienna lista arg tam na dole


def mnoz2(*args):
    wynik = 1
    for liczba in args:
        wynik *= liczba
    print(wynik)


def wylicz(imie1='adam', imie2='ewa', **kwargs):
# ** = słownik zmiennej długości
    print(imie1)
    print(imie2)
    for k, v in kwargs.items():
        print("{} {}".format(k, v))


########## typy argumentów w funkcjach:
# arg pozycyjne wymagane
# arg nazwane wymagane
# arg domyślne (nie są wymagane bo mają jakieś już wartosci)
# arg zmiennej długości: listy, słowniki


def main(args):
    # mnoz(4, 6)
    # mnoz2(1, 2, 3, 4, 5)
    wylicz(imie2='ola', imie3='piotr', imie4='alfons')
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
