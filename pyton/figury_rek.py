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
        rysuj(bok, kat, przyrost, warunek - 1)


def main(args):
    turtle.setup(800, 600)
    turtle.color('blue', 'yellow')
    turtle.begin_fill()
    turtle.speed(10)

    rysuj(bok=100, kat=160, przyrost=10, warunek=170)

    turtle.end_fill()
    turtle.done()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
