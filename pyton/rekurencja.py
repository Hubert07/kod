#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rekurencja.py
#
import turtle


def rysujKwadrat(zolw, bok, ile, kat, granica):
    # ~for i in range(4):
    zolw.forward(bok)
    zolw.right(kat)
<<<<<<< HEAD
    if ile < granica:
        rysujKwadrat(zolw, bok + 2, ile + 1, kat, granica)
=======
    if ile <= granica:
        rysujKwadrat(zolw, bok + 1, ile + 1, kat, granica)

>>>>>>> 57abe1db42a4ce06b640266ad9e28636c1a4ce09


def main(args):
    turtle.title("Kwadraty")
    turtle.setup(1000, 800)

    zolw = turtle.Turtle()
    zolw.color('green')
    zolw.speed(0)

<<<<<<< HEAD
    granica = int(input("Podaj iloś wykonanych obrotów: "))
    rysujKwadrat(zolw, 60, 0, 91, granica)
=======
    rysujKwadrat(zolw, 60, 4, 91, 300)
>>>>>>> 57abe1db42a4ce06b640266ad9e28636c1a4ce09

    turtle.done()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
