#! /usr/bin/env python
# -*- coding: utf-8 -*-
# modele.py

from peewee import *
baza_plik = 'modele.db'
baza = SqliteDatabase(baza_plik)  # instancja bazy

# MODELE DANYCH (jak chcę coś z peewee)
# nazwa klasy zawsze z wielkiej


class BazaModel(Model):
    class Meta:
        database = baza


class Kategoria(BazaModel):
    kategoria = CharField(max_length=30)  # nie pozwalamy żeby nie było nazwy


class Pytanie(BazaModel):
    pytanie = CharField()
    id_kat = ForeignKeyField(Kategoria, related_name='pytania')


class Odpowiedz(BazaModel):
    id_p = ForeignKeyField(Pytanie, related_name='odpowiedzi')
    odpowiedzi = CharField(null=False)
    odpok = BooleanField(default=False)
    plec_naucz = IntegerField()
