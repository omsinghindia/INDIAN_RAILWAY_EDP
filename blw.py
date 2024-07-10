import sqlite3

def connect():
       con = sqlite3.connect('blw.db')
       cur = con.cursor()

       cur.execute('CREATE TABLE IF NOT EXISTS blw(id INTEGER PRIMARY KEY, pid integer PRIMARY KEY , pn text, po text, date integer, \
                    cat text, lts text, total integer, s integer, d integer)')

       con.commit()
       con.close()

def insert(pid = ' ', pn = ' ', po = ' ', date = ' ', cat = ' ', lts = ' ', total = ' ', s = ' ', d = ' '):
       con = sqlite3.connect('blw.db')
       cur = con.cursor()

       cur.execute('INSERT INTO blw VALUES (NULL,?,?,?,?,?,?,?,?,?)',(pid,pn,po,date,cat,lts,total,s,d))

       con.commit()
       con.close()

def view():
       con = sqlite3.connect('blw.db')
       cur = con.cursor()

       cur.execute('SELECT * FROM blw')
       row = cur.fetchall()
       return row

       con.commit()
       

def delete(id):
       con = sqlite3.connect('blw.db')
       cur = con.cursor()

       cur.execute('DELETE FROM blw WHERE id = ?',(id,))

       con.commit()
       con.close()

def update(id,pid = ' ', pn = ' ', po = ' ', date = ' ', cat = ' ', lts = ' ', total = ' ', s = ' ', d = ' '):
       con = sqlite3.connect('blw.db')
       cur = con.cursor()

       cur.execute('UPDATE blw SET pid = ? OR pn = ? OR po = ? OR date = ? OR cat = ? OR lts = ? OR total = ? OR \
                    s = ? OR d = ?',(pid,pn,po,date,cat,lts,total,s,d))


       con.commit()
       con.close()

def search(pid = ' ', pn = ' ', po = ' ', date = ' ', cat = ' ', lts = ' ', total = ' ', s = ' ', d = ' '):
       con = sqlite3.connect('blw.db')
       cur = con.cursor()

       cur.execute('SELECT * FROM blw WHERE  pid = ? OR pn = ? OR po = ? OR date = ? OR cat = ? OR lts = ? OR \
                    total = ? OR s = ? OR d = ?',(pid,pn,po,date,cat,lts,total,s,d))
       row = cur.fetchall()
       return row

       con.commit()
       
connect()


