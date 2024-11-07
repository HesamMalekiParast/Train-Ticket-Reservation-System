# def init_db():
#     engine= create_e
import sqlite3


def  init_db():
    conn = sqlite3.connect('train_tickets.db')
    return conn
def sql_table(conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS stocks
    (train_id int, trans text, symbol text, qty real, price real)''')