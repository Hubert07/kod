#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tabliczka_mnozenia.py
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
#  pyformat.com dobra  strona


def main(args):

    a = int(input("Podaj zakres mnożenia: "))
    b = int(input(" Podaj 2 zakres mnożenia: "))

    for i in range(1, a + 1, 1):  # pętla zewnętrzna
        for j in range(1, b + 1, 1):
            print("{:>4}" .format(i * j), end='')
        print()  # znak końca linii

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
