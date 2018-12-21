#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  quiz.py
#

from flask import g
from modele import *
from views import *


app.config.update(dict(
    SECRET_KEY='7m0lbl6znb8j92lasdqj4jnhlajsd'
))


@app.before_request
def before_request():
    g.db = baza
    g.db.connect()


@app.after_request
def after_request(response):
    g.db.close()
    return response


@app.route("/klasa")
def klasa():
    return render_template('klasa/klasa.html')


if __name__ == '__main__':
    app.run(debug=True)
