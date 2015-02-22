#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test basique de bottle"""

#imports
import bottle
import bottle_sqlite
import sqlite3

#globals
dbpath = '../datas/sqlite.db'

#bottle app
app = bottle.Bottle()
sqlite_plugin = bottle_sqlite.SQLitePlugin(dbfile=dbpath)

@app.route('/')
def hello():
    return 'Hello World - Monde'
    
@app.route('/schema', apply=[sqlite_plugin])
def schema(db):
    ret = ""
    for line in db.iterdump():
        ret += '%s<br/>' % line
    return ret

app.run(reloader=True)

