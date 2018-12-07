#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  quiz.py
#
#  Copyright 2018  <>
from flask import Flask
from flask import render_template
app = Flask(__name__)

print(__name__)


@app.route("/")
def hello():
    return "<h1>Witaj Świecie!</h1><h2>Aplikacja Quiz<h2/>"


@app.route("/strona")
def strona():
    return render_template('html/strona.html')


@app.route("/klasa")
def klasa():
    return render_template('klasa/klasa.html')


if __name__ == '__main__':
    app.run(debug=True)
