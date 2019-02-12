#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kompresja.py
#


def main(args):
    Vk = input("Rozmiar danych skompresowanych (B): ")
    Vnk = input("Rozmiar danych nieskompresowanych (B): ")
    Rc = int(Vk) / int(Vnk) * 100
    R2c = 1 - int(Vk) / int(Vnk) * 100

    print("O ile zmniejszyły się dane: ")
    print("Ile miejsca zaoszczędzonow: ")

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
