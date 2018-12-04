#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  uczniowie_orm.py
#
import os
from modele import *

def dodaj_dane(dane):


def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect()  # połączenie z bazą
    baza.create_tables([Klasa, Uczen, Przedmiot, Ocena])

    dane = {
        # to na górze to słownik
        # klucz: wartość,
        Klasa: 'klasy',
        Uczen: 'uczniowie',
        Przedmiot: 'przedmioty',
        Ocena: 'oceny',
    }

    baza.close()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
