#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# hermatyzacja danych - ukrycie ich = nie mozna ich zmienić zewnętrznie
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
            self.__plec = "k"
            self.__atak = 3
            self.__blok = 2
        else:
            self.__plec = "m"
            self.__atak = 9
            self.__blok = 3

    def atakuj(self, osoba):
        osoba.blokuj(self.__atak)

    def blokuj(self, atak):
        self.hp -= (atak - self.__blok)
        if self.hp < 1:
            print("I'm dead")
        else:
            print("Hit me baby one more time")


halina = Osoba('Halina', 'Gwizd', 10)
print(halina.__dict__)
print(halina.imie, halina.nazwisko, halina.plec, halina.hp)

michal = Osoba('Michal', 'Świst', 10)
print(michal.imie, michal.nazwisko, michal.plec, michal.hp)

print("Walka!")
halina.atakuj(michal)
michal.atakuj(halina)
halina.atakuj(michal)
halina.atakuj(michal)
halina.atakuj(michal)
print(halina.hp, michal.hp)
