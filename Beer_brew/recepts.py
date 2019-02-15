import beer
import sqlite3

connection=sqlite3.connect('beer.db')
cur = connection.cursor()


def cleaning():
    beer.txt_opisanie.clear()
    beer.txt_recept.clear()
    beer.txt_ruls.clear()
    beer.txt_haract.clear()

def run_beer(sort_beer):
    cur.execute("SELECT * FROM table1 WHERE name=%s"%("'"+sort_beer+"'"));
    q = cur.fetchall()[0]
    cleaning()
    beer.lbl_name['text']=q[1]
    beer.txt_opisanie.write(q[2])
    beer.txt_recept.write(q[3])
    beer.txt_ruls.write(q[5])
    beer.txt_haract.write(q[4])


