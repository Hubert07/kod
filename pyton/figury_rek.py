#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rekurencja.py
#
import turtle


def rysuj(bok, kat, przyrost, warunek):
    turtle.forward(bok)
    turtle.right(kat)
    if kat < warunek:
        rysuj(bok + 1, kat, przyrost, warunek + 1)


def main(args):
    turtle.setup(1000, 900)
    turtle.color('black', 'yellow')
    turtle.begin_fill()
    turtle.speed(0)

    rysuj(bok=150, kat=105, przyrost=10, warunek=180)

    turtle.end_fill()
    turtle.done()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
