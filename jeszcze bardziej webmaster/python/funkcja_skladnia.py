#! /usr/bin/env python
# -*- coding: utf-8 -*-

a, b = 5, 10
print(a + b)
# zmienna (variable) globalna
# zasięg globalny (global)
# przestrzeń modułu (namespace)


def sumuj1():
# nowa przestrzeń nazwy, przestrzeń funkcji
    print(a + b)


def main(args):
    global a, b
    a, b = 2, 3  # zmienne lokalne z zasięgiem lokalnym
    print(a + b)
    sumuj1()
    return 0



def odejmij(a, b):
    print(a - b)
    a, b = 4, 4


def odejmij2(lista):
    lista.append(lista[0] - lista[1])


def main2(args):
    # a, b = 2, 3
    # print(a - b)
    # odejmij(a, b)
    # odejmij2(a, b)
    # print(a - b)
    l = [3, 4]
    odejmij2(l)
    print(l)
    return 0


if __name__ == '__main__':
# skrypt został uruchomiony a nie zaimportowany
    import sys
    sys.exit(main2(sys.argv))
