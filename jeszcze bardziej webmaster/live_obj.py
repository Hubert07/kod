#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import sys
from random import randint


class Plansza():
    """ Plansza gry """

    def __init__(self, szer, wys):
        """ Konstruktor, przygotowanie okna gry """
        self.pow = pygame.display.set_mode((szer, wys), 0, 32)
        self.szer, self.wys = szer, wys
        pygame.display.set_caption('Life')

    def rysuj(self, *args):
        """ Rysowanie okna gry """
        # kolor okna gry, składowe RGB podane w tupli
        self.pow.fill((0, 0, 0))
        for obj in args:
            obj.rysuj_na(self.pow)

        pygame.display.update()


class LifeGra(object):
    """ Kontroler gry """

    def __init__(self, szer, wys, roz=10):
        pygame.init()
        self.plansza = Plansza(szer * roz, wys * roz)
        self.populacja = Populacja(szer, wys, roz)
        self.fpsClock = pygame.time.Clock()

    def uruchom(self):
        """ Główna pętla programu """
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit(0)

            if event.type == MOUSEMOTION or event.type == MOUSEBUTTONDOWN:
                self.populacja.obsluz_mysze()

            if event.type == KEYDOWN and event.key == K_RETURN:
                self.uruchomiona = True

            # if event.type == KEYDOWN and event.key == K_RETURN:
            #     self.uruchomiona = False

            self.plansza.rysuj(self.populacja)

            if getattr(self, "uruchomiona", None):
                self.populacja.wylicz_generacje()
            self.fpsClock.tick(10)


DEAD = 0
ALIVE = 1


class Populacja():
    def __init__(self, szer, wys, roz=10):
        self.roz, self.szer, self.wys = roz, szer, wys
        self.generacja = self.utworz_generacje()

    def utworz_generacje(self):
        # generacja = []
        # for x in range(self.szyr):
        #     kolumna = []
        #     for y in range(self.wys):
        #         kolumna.append(DEAD)
        #     generacja.append(kolumna)
        #   robimy tam macierz V
        return [[DEAD for y in range(self.wys)] for x in range(self.szer)]

    def obsluz_mysze(self):
        przyciski = pygame.mouse.get_pressed()
        if not any(przyciski):
            return
        x, y = pygame.mouse.get_pos()
        x /= self.roz
        y /= self.roz

        stan = True if przyciski[0] else False
        print(stan)
        self.generacja[int(x)][int(y)] = ALIVE if stan else DEAD

    def rysuj_na(self, pow):
        for x, y in self.zywe_komorki():
            roz = (self.roz, self.roz)
            pozycja = (x * self.roz, y * self.roz)
            kolor = (255, randint(0, 255), randint(0, 255))
            pygame.draw.rect(pow, kolor, Rect(pozycja, roz))

    def zywe_komorki(self):
        """" Generator zwracający współrzędne żywych komórek """
        for x in range(len(self.generacja)):
            kolumna = self.generacja[x]
            for y in range(len(kolumna)):
                if kolumna[y] == ALIVE:
                    yield x, y

    def zwroc_sasiada(self, x, y):
        for i in range(x - 1, x + 2, 1):
            for j in range(y - 1, y + 2, 1):
                if i == x and j == y:
                    continue  # pomijanie
                if i >= self.szer:
                    i = 0
                elif i < 0:
                    i = self.szer - 1

                if j >= self.wys:
                    j = 0
                elif j < 0:
                    j = self.wys - 1

                yield self.generacja[i][j]

    def wylicz_generacje(self):
        """ Wyliczamy następną generację populacji """
        nowa_gen = self.utworz_generacje()

        for x in range(len(self.generacja)):
            kolumna = self.generacja[x]
            for y in range(len(kolumna)):
                ileZywych = sum(self.zwroc_sasiada(x, y))
                if ileZywych == 3:
                    nowa_gen[x][y] = ALIVE
                elif ileZywych == 2:
                    nowa_gen[x][y] = kolumna[y]
                else:
                    nowa_gen[x][y] = DEAD

        self.generacja = nowa_gen


if __name__ == "__main__":
    gra = LifeGra(80, 40)
    gra.uruchom()
