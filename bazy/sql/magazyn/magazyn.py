#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import csv


def dane_z_pliku(nazwa_pliku):
    dane = []  # taki nawias to pusta lista
    with open(nazwa_pliku, 'r', newline='', encoding='utf-8') as plik:
            tresc = csv.reader(plik, delimiter='\t')
            for rekord in tresc:
                rekord = [x.strip() for x in rekord]  # usuwa puste,
            # niepotrzebna znaki (tralling spaces)
                dane.append(rekord)  # dodawanie rekordów do listy
    return dane


def main(args):
    con = sqlite3.connect('magazyn.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora

    # utworzenie tabeli w bazie
    # with open('apps.sql', 'r') as plik:
    #     cur.executescript(plik.read())

    # dodawanie danych do bazy

    dane = dane_z_pliku('dane_orders.txt')
    print(dane)
    dane.pop(0)  # usuń 1 rekord z listy
    cur.executemany('INSERT INTO tbOrders VALUES(?, ?, ?, ?)', dane)

    dane = dane_z_pliku('dane_customers.txt')
    print(dane)
    dane.pop(0)  # usuń 1 rekord z listy
    cur.executemany('INSERT INTO tbCustomers VALUES(?, ?, ?)', dane)

    dane = dane_z_pliku('dane_subscriptions.txt')
    print(dane)
    dane.pop(0)  # usuń 1 rekord z listy
    cur.executemany('INSERT INTO tbSubscription VALUES(?, ?, ?, ?)', dane)
    # ? = zastępnik

    con.commit()  # zatwirdzenie w bazie
    con.close()  # zamknięcie bazy
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
