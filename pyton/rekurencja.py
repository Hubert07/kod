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
    if ile <= granica:
        rysujKwadrat(zolw, bok + 1, ile + 1, kat, granica)



def main(args):
    turtle.title("Kwadraty")
    turtle.setup(1000, 800)

    zolw = turtle.Turtle()
    zolw.color('green')
    zolw.speed(0)

    rysujKwadrat(zolw, 60, 4, 91, 300)

    turtle.done()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
