#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# abc.py
# złożona funkcja warunkowa na 3 warunki
#
# Program pobiera 3 liczbu do użytkownika
# a następnie wyświetla liczbę największą można używać and/or


def max(a, b, c)
    m = None
    if a > b:
        if a > c:
            m = a
    print("Największa: ", m)
    return m


def main(args):

    assert(maks(1, 2, 3) == 3)
    # a = int(input("Podaj pierwszą liczbę: "))
    # b = int(input("Podaj drugą liczbę: "))
    # c = int(input("Podaj trzecią liczbę: "))

    # if a > b and a > c:
    #     print(a, "Jest największą liczbą")

    # elif b > c and b > a:
    #     print(b, "Jest największą liczbą")

    # else:
    #     print(c, "Jest największą liczbą")

    # if a > b:
    #     print(a, "Jest większe od", b)
    #     print(a, "Jest różne od", b)

    # elif a < b:
    #     print(b, "Jest większe od", a)
    #     print(a, "Jest różne od", b)

    # else:
    #     print(a, "Jest równe", b)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
