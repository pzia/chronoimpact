#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Import/export from db in ../datas/sqlite.db
Usage :
* load db : ./dodb.py load [filename.sql] (default to create.sql)
* dump db : ./dodb.py dump filename.sql"""

import sys
import sqlite3

dbpath = "../datas/sqlite.db"
loaddefault = "create.sql"

def dumpsql(what):
    con = sqlite3.connect(dbpath)
    with open(what, 'w') as f:
        for line in con.iterdump():
            f.write('%s\n' % line)

def loadsql(what):
    con = sqlite3.connect('../sqlite.db')
    f = open(what,'r')
    sql = f.read() # watch out for built-in `str`
    con.executescript(sql)
    
if not (len(sys.argv) > 1) :
    print(__doc__)
    sys.exit()

if sys.argv[1] == 'load' :
    if len(sys.argv) > 2:
        loadsql(sys.argv[2])
    else :
        loadsql(loaddefault)
elif sys.argv[1] == 'dump' and len(sys.argv) > 2:
    dumpsql(sys.argv[2])

