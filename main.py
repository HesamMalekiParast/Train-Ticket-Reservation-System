# def init_db():
#     engine= create_e
import sqlite3


def  init_db():
    conn = sqlite3.connect('train_tickets.db')
    return conn
def sql_table(conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS stocks
    (train_id int, train_name varchar, departure_time date, destination varchar(254), availableseats int)''')
    conn.commit()
    c.execute("SELECT * FROM stocks")
    print(c.fetchall())
conn=init_db()
sql_table(conn)