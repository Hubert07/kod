#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  stos_str.py
#
#  Stos powinien być zainicjowany


def push(stos, rozmiar, SP, dane):
    if SP < rozmiar:
        stos[SP] = dane
        SP += 1
    else:
        print("Stack overflow")

    return SP


def pop(stos, rozmiar, SP):
    element = None
    SP -= 1
    if SP >= 0:
        element = stos[SP]
        stos[SP] = None
    else:
        print("Stack overflow")

    return SP, element


def main(args):
    stos = []
    SP = 0
    rozmiar = 3

    stos = [None] * rozmiar
    SP = push(stos, rozmiar, SP, 2)
    SP = push(stos, rozmiar, SP, 5)
    SP, element = pop(stos, rozmiar, SP)
    print(element)

    SP = push(stos, rozmiar, SP, 4)
    SP, element = pop(stos, rozmiar, SP)
    print(element)

    SP, element = pop(stos, rozmiar, SP)
    print(element)

    SP, element = pop(stos, rozmiar, SP)
    print(element)
    print(SP)
    print(stos)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
