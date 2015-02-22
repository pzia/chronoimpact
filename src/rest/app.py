#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Service Rest pour chronodatas"""

#imports
import json
import bottle
import bottle_sqlite
import sqlite3

#globals
dbpath = '../datas/sqlite.db'

#bottle app
app = bottle.Bottle()
sqlite_plugin = bottle_sqlite.SQLitePlugin(dbfile=dbpath)

@app.route('/')
def documentation():
    """Autodocumentation de l'api"""
    liste = []
    for route in app.routes:
        r = {}
        r['method'] = route.method
        r['rule'] = route.rule
        r['doc'] = route.callback.__doc__
        liste.append(r)
    #return json.dumps(ret) #FIXME : comment diriger le format souhaité, ici fournir du html quand on arrive avec un browser ?
    ret = "%s<hr/>" % bottle.request.path
    for l in liste :
        ret += "<b>%s</b>&nbsp;<i><a href=\"%s\">%s</a></i>&nbsp;\"%s\"<br/>" % (l['method'], l['rule'], l['rule'], l['doc'])
    return ret

@app.get('/groups', apply=[sqlite_plugin])
def groups(db):
    """Liste les groupes de projets"""
    rows = []
    for row in db.execute('SELECT * FROM groups'):
        rows.append(dict(row))
    return json.dumps({'groups': rows})
    
@app.route('/dump', apply=[sqlite_plugin])
def dump(db):
    """Renvoi l'export complet des données"""
    ret = ""
    for line in db.iterdump():
        ret += '%s<br/>' % line
    return ret

app.run(reloader=True)

