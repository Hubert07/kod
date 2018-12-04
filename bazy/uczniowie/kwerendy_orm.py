#! /usr/bin/env python
# -*- coding: utf-8 -*-

from modele import *


def kw01():
    obj = Uczen.select().where(Uczen.imie == 'Rafał')
    for row in obj:
        print(row.imie, row.nazwisko)


def main(atgs):
    baza.connect()

    kw01()

    baza.close()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
