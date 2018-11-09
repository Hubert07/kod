#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  orm_peewee.py
#

import os
from peewee import *
baza_plik = 'test.db'
baza = SqliteDatabase(baza_plik)  # instancja bazy

### MODELE DANYCH (jak chcę coś z peewee) ###
# nazwa klasy zawsze z wielkiej


class BazaModel(Model):
    class Meta:
        database = baza


class Klasa(BazaModel):
    nazwa = CharField(null=False)  # nie pozwalamy żeby nie było nazwy
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)

    # class Meta:
    #     database = baza  # w której db to coś funkcjonuje


class Uczen(BazaModel):
    imie = CharField(null=False)  # nie pozwalamy żeby nie było nazwy
    nazwisko = CharField(null=False)  # nie pozwalamy żeby nie było nazwy
    plec = BooleanField()
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')

    # class Meta:
    #     database = baza


class Wynik(BazaModel):
    egzaminhum = FloatField(default=o)  # nie pozwalamy żeby nie było nazwy
    egzaminmat = FloatField(default=o)  # nie pozwalamy żeby nie było nazwy
    egzaminjez = FloatField(default=o)  # nie pozwalamy żeby nie było nazwy
    uczen = ForeignKeyField(Uczen, related_name='wyniki')


def main(args):
    if os.path_exsist(baza_plik):
        os.remove(baza_plik)
    baza.connect()  # połączenie z bazą
    baza.create_tables([Klasa, Uczen, Wynik])
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
