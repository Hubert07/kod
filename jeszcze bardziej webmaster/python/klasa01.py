#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# klasa01.py


class Osoba():
    """ Prosta klasa opisująca osobę każda metoda w klasie ma (slef)"""

    def __init__(self, imie, nazwisko, hp):
        self.imie = imie
        self.nazwisko = nazwisko
        self.ustawPlec(imie)
        self.hp = hp

    def ustawPlec(self, imie):
        if imie[-1] == "a":
            self.plec = "k"
            self.atak = 3
            self.blok = 2
        else:
            self.plec = "m"
            self.atak = 9
            self.blok = 3

    def atakuj(self, osoba):
        osoba.blokuj(self.atak)

    def blokuj(self, atak):
        self.hp -= (atak - self.blok)
        if self.hp < 1:
            print("I'm dead")
        else:
            print("Hit me baby one more time")


halina = Osoba('Halina', 'Gwizd', 100)
print(halina.imie, halina.nazwisko, halina.plec, halina.hp)
michal = Osoba('Michaś', 'Świst', 95)
print(michal.imie, michal.nazwisko, michal.plec, michal.hp)
halina.atakuj(michal)
michal.atakuj(halina)
halina.atakuj(michal)
halina.atakuj(michal)
halina.atakuj(michal)
print(halina.hp, michal.hp)
