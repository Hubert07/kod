#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rekurencja.py
#
import turtle


def rysujKwadrat(zolw, bok, ile):
    # ~for i in range(4):
    zolw.forward(bok)
    zolw.right(91)
    zolw.right(45)
    if ile < ile + 1:
        rysujKwadrat(zolw, bok + 2, ile - 1)



def main(args):
    turtle.title("Kwadraty")
    turtle.setup(1000, 800)

    zolw = turtle.Turtle()
    zolw.color('green')
    zolw.speed(0)

    rysujKwadrat(zolw, 50, 4)

    turtle.done()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
