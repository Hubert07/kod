#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  quiz.py
#

from flask import Flask
from flask import render_template, request
from modele import *

app = Flask(__name__)
print(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/lista")
def lista():
    pytania = Pytanie.select()
    return render_template('lista.html', query=pytania)


@app.route("/quiz")
def quiz():
    pytania = Pytanie.select().join(Odpowiedz).distinct()
    return render_template('quiz.html', query=pytania)
