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
    nazwa = CharField(null=False)
    # nie pozwalamy żeby nie było nazwy
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)

    # class Meta:
    #     database = baza  # w której db to coś funkcjonuje


class Uczen(BazaModel):
    imie = CharField(null=False)  # nie pozwalamy żeby nie było nazwy
    nazwisko = CharField(null=False)  # nie pozwalamy żeby nie było nazwy
    plec = BooleanField()
    # roknaboru = IntegerField(default=0)
    # rokmatury = IntegerField(default=0)
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')

    # class Meta:
    #     database = baza


class Wynik(BazaModel):
    egzaminhum = FloatField(default=0)  # nie pozwalamy żeby nie było nazwy
    egzaminmat = FloatField(default=0)  # nie pozwalamy żeby nie było nazwy
    egzaminjez = FloatField(default=0)  # nie pozwalamy żeby nie było nazwy
    uczen = ForeignKeyField(Uczen, related_name='wyniki')


def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect()  # połączenie z bazą
    baza.create_tables([Klasa, Uczen, Wynik])

    kl2a = Klasa(nazwa='2A', roknaboru=2017, rokmatury=2020)
    kl1a = Klasa(nazwa='1A', roknaboru=2009, rokmatury=2012)

    kl2a.save()
    kl1a.save()

    u1 = Uczen(imie='Hubert', nazwisko='Gajewski', plec=False, klasa=kl2a)
    u2 = Uczen(imie='Marian', nazwisko='Paździoch', plec=False, klasa=kl1a)
    u3 = Uczen(imie='Helena', nazwisko='Paździochowa', plec=True, klasa=kl1a)

    u1.save()
    u2.save()
    u3.save()

    uczniowie = Uczen.select()
    for uczen in uczniowie:
        print(uczen.id, uczen.nazwisko, uczen.klasa.nazwa)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
