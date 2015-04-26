#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Service web pour chronodatas (jtable api)"""

#imports
import json
import bottle
import bottle_sqlite
import sqlite3
import webbrowser

#globals
dbpath = '../datas/sqlite.db'
apppath = '../app'
fieldsRef = {
    'groups' : ['name', 'date_start', 'date_end'],
    'projects' : ['name', 'id_group', "date_impact"],
    'locations' : ['name'],
    'impacts' : ['id_project', 'id_location', 'type', 'real', 'felt'],
}

#bottle app
app = bottle.Bottle()
sqlite_plugin = bottle_sqlite.SQLitePlugin(dbfile=dbpath)

def tableKey(table):
    return "id_"+table[:-1]

@app.route('/app/<filename:path>')
def send_static(filename):
    return bottle.static_file(filename, root=apppath)

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

@app.post('/<table:re:[a-z]+>/list', apply=[sqlite_plugin])
def listing(table, db):
    """Liste les lignes d'une table"""
    rows = []
    for row in db.execute("SELECT * FROM %s" % table):
        rows.append(dict(row))
    res = {}
    res['Result'] = 'OK'
    res['Records'] = rows        
    return json.dumps(res)

@app.post('/<table:re:[a-z]+>/options/<option:re:[a-z]+>', apply=[sqlite_plugin])
def options(table, option, db):
    """Liste les lignes d'une table"""
    rows = []
    for row in db.execute("SELECT * FROM %s" % table):
        r = dict(row)
        rows.append({'DisplayText' : r[option], 'Value' : r[tableKey(table)]})
    res = {}
    res['Result'] = 'OK'
    res['Options'] = rows        
    return json.dumps(res)


@app.post('/<table:re:[a-z]+>/<parent:re:[a-z]+>/<ID:int>', apply=[sqlite_plugin])
def projects(table, parent, ID, db):
    """Liste les lignes d'une table relative à un parent"""
    rows = []
    for row in db.execute("SELECT * FROM %s WHERE %s = %d" % (table, tableKey(parent), int(ID))):
        rows.append(dict(row))
    res = {}
    res['Result'] = 'OK'
    res['Records'] = rows        
    return json.dumps(res)

@app.post('/<table:re:[a-z]+>/create', apply=[sqlite_plugin])
def create(table, db):
    """crée un enregistrement"""
    fields = fieldsRef[table]
    vals = []
    for field in fields :
        vals.append(bottle.request.forms.get(field))
    sql = "INSERT INTO %s (" % table
    sql += ",".join(fields)
    sql += ") VALUES ("
    sql += "'"+"', '".join(vals)+"'"
    sql += ");"
    db.execute(sql)
    row = db.execute("SELECT * FROM %s WHERE %s = last_insert_rowid()" % (table, tableKey(table))).fetchone();
    res = {
        'Result' : 'OK',
        'Record' : dict(row)
    }
    return json.dumps(res)

@app.post('/<table:re:[a-z]+>/update', apply=[sqlite_plugin])
def update(table, db):
    """mis à jour un enregistrement"""
    fields = fieldsRef[table]
    vals = []
    for field in fields :
        vals.append("%s = '%s'" % (field, bottle.request.forms.get(field)))
    sql = "UPDATE %s SET " % table
    sql += ", ".join(vals)
    sql += " WHERE %s = %d;" % (tableKey(table), int(bottle.request.forms.get(tableKey(table))))
    db.execute(sql)
    row = db.execute("SELECT * FROM %s WHERE %s = last_insert_rowid()" % (table, tableKey(table))).fetchone();
    return json.dumps({'Result' : 'OK'})

@app.post('/<table:re:[a-z]+>/delete', apply=[sqlite_plugin])
def delete_group(table, db):
    """Efface"""
    row = db.execute('DELETE FROM %s WHERE %s = %d' % (table, tableKey(table), int(bottle.request.forms.get(tableKey(table)))))
    return json.dumps({'Result' : 'OK'})

@app.route('/dump', apply=[sqlite_plugin])
def dump(db):
    """Renvoi l'export complet des données"""
    ret = ""
    for line in db.iterdump():
        ret += '%s<br/>' % line
    return ret

#webbrowser.open("http://127.0.0.1:8080/app/index.html")
app.run(reloader=True)

