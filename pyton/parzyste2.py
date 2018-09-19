#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  parzyste.py
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
#  liczba parzysta jest traktowana jako TRUE a nieparxysta jako FALSE
#
#


def main(args):
    x = int(input("Podaj zakres liczb: "))
    y = int(input("Podaj od której liczby chcesz zacząć: "))

    if y > x:
            print("Pierwsza liczba ma być większa orzeszku", x, y)

    for liczba in range(y, x):
        # if liczba % 2 == 0:
        if not liczba % 2:
            print(liczba)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
