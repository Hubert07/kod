#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import sys


class Plansza():
    """ Plansza gry """

    def __init__(self, szer, wys):
        """ Konstruktor, przygotowanie okna gry """
        self.szer, self.wys = szer, wys
        self.pow = pygame.display.set_mode((szer, wys), 0, 32)
        pygame.display.set_caption('Pong')

    def rysuj(self, *args):
        """ Rysowanie okna gry """
        # kolor okna gry, składowe RGB podane w tupli
        self.pow.fill((0, 0, 0))
        for obGraf in args:
            self.pow.blit(obGraf.pow, obGraf.prost)
        pygame.display.update()


class PongGra(object):
    """ Kontroler gry """

    def __init__(self, szer, wys):
        pygame.init()
        self.plansza = Plansza(szer, wys)
        self.pal1 = Paletka(szer=100, wys=5, x=350, y=360)
        self.pal2 = Paletka(szer=100, wys=5, x=350, y=60)
        self.pilka = Pilka(szer=30, wys=30, x=400, y=200)
        self.gracz2 = Gracz2(self.pal2, self.pilka, 5)
        self.fpsClock = pygame.time.Clock()

    def uruchom(self):
        """ Główna pętla programu """
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == MOUSEMOTION:
                    mX, mY = event.pos
                    self.pal1.przesun(mX, self.plansza.szer)


            self.pilka.ruszaj(self.plansza.szer, self.plansza.wys, self.pal1, self.pal2)
            self.gracz2.ruszaj()
            self.plansza.rysuj(
                               self.pal1,
                               self.pal2,
                               self.pilka
                               )
            self.fpsClock.tick(30)


class ObiektGraf():
    """ Klasa bazowa dla rysowanych obiektów """
    def __init__(self, szer, wys, x, y, kolor=(1, 1, 1)):
        self.szer = szer
        self.wys = wys
        self.pow = pygame.Surface([szer, wys], pygame.SRCALPHA).convert_alpha()
        self.prost = self.pow.get_rect(x=x, y=y)
        self.kolor = kolor


class Paletka(ObiektGraf):
    def __init__(self, szer, wys, x, y, kolor=(255, 255, 255), makx_v=1):
        super().__init__(szer, wys, x, y, kolor)
        self.pow.fill(self.kolor)
        self.makx_v = makx_v
        self.start_x = x
        self.start_y = y

    def przesun(self, mX, o_szer):
        """
        :param:
        mX = składowa X pozycji paletki
        o_szer = szeroknoścokna gry
        """
        przesuniecie = mX - self.makx_v
        if przesuniecie > o_szer - self.szer:
            przesuniecie = o_szer - self.szer
        if przesuniecie < 0:
            przesuniecie = 0
        self.prost.x = przesuniecie


class Pilka(ObiektGraf):
    def __init__(self, szer, wys, x, y, kolor=(255, 255, 255), px_v=10, py_v=8):
        super().__init__(szer, wys, x, y, kolor)
        self.px_v = px_v
        self.py_v = py_v
        pygame.draw.ellipse(self.pow, self.kolor, [0, 0, self.szer, self.wys])

    def ruszaj(self, o_szer, o_wys, *args):
        self.prost.move_ip(self.px_v, self.py_v)
        if self.prost.right >= o_szer or self.prost.left <= 0:
            self.px_v *= -1

        if self.prost.bottom >= o_wys or self.prost.top <= 0:
            self.prost.x = o_szer / 2
            self.prost.y = o_wys / 2

        for pal in args:
            if self.prost.colliderect(pal.prost):
                self.py_v *= -1


class Gracz2():
    def __init__(self, pal, pilka, pal_v=10):
        self.pal = pal
        self.pilka = pilka
        self.pal_v = pal_v

    def ruszaj(self):
        if self.pilka.prost.centerx > self.pal.prost.centerx:
            self.pal.prost.x += self.pal_v
        elif self.pilka.prost.centerx < self.pal.prost.centerx:
            self.pal.prost.x -= self.pal_v


if __name__ == "__main__":
    gra = PongGra(800, 400)
    gra.uruchom()
