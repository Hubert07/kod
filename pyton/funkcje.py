#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wejscie_wyjscie.py
#
#  Copyright 2018  <>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  duck typing = you must be like duck
# pass = zaraz uzupełnię
# zasięg zmiennych jeżeli definiujesz zmienną w funkvji, to ma ona
# zasięg lokalny ograniczny nazwą funkcji
#


def suma(a, b):
    return a + b


def roznica(a, b):
    return a - b


def iloczyn(a, b):
    return a * b


def iloraz(a, b):
    return a / b


def main(args):
    # To na dole = temu co jest w cpp
    a = int(input("podaj liczbę:"))
    b = int(input("podaj drugą liczbę:"))

    print("Suma: ", suma(a, b))
    print("Różnica: ", roznica(a, b))
    print("Iloczyn: ", iloczyn(a, b))
    print("Iloraz: ", iloraz(a, b))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
