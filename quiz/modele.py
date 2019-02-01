#! /usr/bin/env python
# -*- coding: utf-8 -*-
# modele.py

from peewee import *
baza_plik = 'quiz.db'
baza = SqliteDatabase(baza_plik)  # instancja bazy

# MODELE DANYCH (jak chcę coś z peewee)
# nazwa klasy zawsze z wielkiej


class BazaModel(Model):
    class Meta:
        database = baza


class Kategoria(BazaModel):
    kategoria = CharField(null=False)  # nie pozwalamy żeby nie było nazwy


class Pytanie(BazaModel):
    pytanie = CharField()
    id_kat = ForeignKeyField(Kategoria, related_name='pytania')


class Odpowiedz(BazaModel):
    odpowiedzi = CharField(null=False)
    id_p = ForeignKeyField(Pytanie, related_name='odpowiedzi')
    odpok = BooleanField(default=False)


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
