#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  uczniowie_orm.py
#
import os
from peewee import *
baza_plik = 'uczniowie.db'
baza = SqliteDatabase(baza_plik)  # instancja bazy

# MODELE DANYCH (jak chcę coś z peewee)
# nazwa klasy zawsze z wielkiej


class BazaModel(Model):
    class Meta:
        database = baza


class Klasa(BazaModel):
    klasa = CharField(max_length=2)  # nie pozwalamy żeby nie było nazwy
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)


class Uczen(BazaModel):
    imie = CharField(null=False)  # nie pozwalamy żeby nie było nazwy
    nazwisko = CharField(null=False)  # nie pozwalamy żeby nie było nazwy
    plec = BooleanField()
    id_klasa = ForeignKeyField(Klasa, related_name='uczniowie')
    egz_hum = FloatField(default=0)
    egz_mat = FloatField(default=0)
    egz_jez = FloatField(default=0)


class Przedmiot(BazaModel):
    przedmiot = CharField(max_length=15)
    imie_naucz = CharField(null=False)
    nazwisko_naucz = CharField(null=False)
    plec_naucz = BooleanField()


class Ocena(BazaModel):
    datad = DateField()
    id_uczen = ForeignKeyField(Uczen, related_name='ocena')
    id_przedmiot = ForeignKeyField(Przedmiot, related_name='przedmiot')
    ocena = DecimalField()


def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect()  # połączenie z bazą
    baza.create_tables([Klasa, Uczen, Przedmiot, Ocena])
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
