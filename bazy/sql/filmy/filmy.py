#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import csv


def dane_z_pliku(nazwa_pliku):
    dane = []  # taki nawias to pusta lista
    with open(nazwa_pliku, 'r', newline='', encoding='utf-8') as plik:
        # tutaj dodaje się różne takie do określenia danych poczytaj o csv
        # (o separatorach w plikach txt)  https://gist.github.com/lo1cgsan
        tresc = csv.reader(plik, delimiter='\t')  # /t separaor to tabulator
        for rekord in tresc:
            rekord = [x.strip()for x in rekord]
            # coś.nazwafunkcji wywołuje tę funkcję dla x
            # [x.strip()for x in rekord] usuwa puste miejsce
            dane.append(rekord)  # append = dodaj
    return dane


def kwerenda_1(cur):
    cur.execute("""
        SELECT name AS nazwa,  genre AS gatunek FROM filmy;
    """)

    wyniki = cur.fetchall()  # pobranie wsyzstkich rekordów na raz
    for row in wyniki:  # wczytanie kolejnych rekordów
        print(tuple(row))  # drukownaie pól


def main(args):

    con = sqlite3.connect('filmy.db')  # połączenie z bazą danych
    cur = con.cursor()  # tworzenie kursora?

    # utworzenie tabeli w bazie danych
    with open('filmy.sql', 'r') as plik:  # otwarcie czegoś tam
        cur.executescript(plik.read())

    # dodawanie danych do bazy
    tbFilmy = dane_z_pliku('filmy.txt')
    tbFilmy.pop(0)  # usuń 1st rekord z listy
    cur.executemany('INSERT INTO tbFilmy VALUES(?, ?, ?, ?, ?)', tbFilmy)
    # ? = zastępnik
    con.commit()  # zatwierdzeniezmian w bazie
    con.close()  # zamknięcie połączenia z bazą

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
