#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  car.py
#
#  napisz definicję obiektu samochód z naastępującymi atrybutami:
#  marka
#  model
#  rok produkcji
#  nadwozie
#  metody obiektu:
#  wiek zwara wiek auta w latach
from datetime import date

dzis = date.today().year


class Samochod():

    def __init__(self, marka, model, rokProdukcji, nadwozie):
        self.marka = marka
        self.model = model
        self.rokProdukcji = rokProdukcji
        self.wiek(rokProdukcji)
        self.nadwozie = nadwozie

    def wiek(self):
        return date.today.year - self.rokProdukcji


camaro = Samochod('Chevrolet', 'Camaro_SS', '1969', 'coupe')
print(camaro.__dict__)
print(camaro.wiek)
