#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy.py

import sqlite3


def kwerenda1(cur):
    cur.execute("""
        WITH srednie AS (
            SELECT nazwisko, imie, AVG(ocena) AS poile FROM uczniowie
            INNER JOIN oceny ON uczniowie.id=oceny.id_uczen
            GROUP BY uczniowie.id
        ) SELECT nazwisko, imie, poile FROM srednie 
        WHERE poile >= 4.0
    """)
    # SELECT klasa, COUNT(uczniowie.id) AS ile FROM klasy INNER JOIN uczniowie ON klasy.id=uczniowie.id_klasa GROUP BY klasa ORDER BY ile DESC
    # SELECT klasa, nazwisko, imie, egz_mat FROM klasy INNER JOIN uczniowie ON klasy.id=uczniowie.id_klasa WHERE klasa='1A'
    # WHERE plec=1
    # WHERE imie LIKE '%a'
    # SELECT nazwisko, imie, egz_hum, egz_mat FROM uczniowie ORDER BY egz_hum DESC LIMIT 5
    # SELECT * FROM uczniowie WHERE nazwisko='Piasecki'
    # SELECT egz_hum, egz_mat FROM uczniowie WHERE nazwisko='Piasecki' AND imie='Rafał'
    # SELECT * FROM uczniowie WHERE nazwisko='Piasecki' AND imie='Rafał'
    # SELECT COUNT(*) FROM uczniowie WHERE nazwisko LIKE 'G%'

    wyniki = cur.fetchall()
    for row in wyniki:
        print(row)


def main(args):
    baza_nazwa = 'uczniowie'
    tabele = ['uczniowie', 'klasy', 'przedmioty', 'oceny']

    con = sqlite3.connect(baza_nazwa + '.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora

    kwerenda1(cur)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))