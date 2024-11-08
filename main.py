import sqlite3

conn = sqlite3.connect('tickets.db')
cursor = conn.cursor()

create_table_query = """  
    CREATE TABLE IF NOT EXISTS train (  
        train_id INTEGER PRIMARY KEY,  
        train_name varchar NOT NULL, 
        origin varchar not null,
        destination varchar not null,
        available_seats   integer not null ,
        time_date date not null
            );  
"""
create_table_reserve = """  
    CREATE TABLE IF NOT EXISTS reservations (  
    reservation_id INTEGER PRIMARY KEY,  
    seat_number INTEGER NOT NULL,  
    status INTEGER CHECK(status IN (1, 2)),  -- وضعیت می‌تواند 1 یا 2 باشد  
    train_id INTEGER NOT NULL,  
    passenger_id INTEGER NOT NULL,  
    date_reserve DATE NOT NULL,  
    FOREIGN KEY (train_id) REFERENCES train(train_id),  
    FOREIGN KEY (passenger_id) REFERENCES passengers(passenger_id)  
);  
"""
create_table_passengers = """  
    CREATE TABLE IF NOT EXISTS passengers (  
        passenger_id INTEGER PRIMARY KEY,  
        passenger_name varchar NOT NULL, 
        passenger_phone  varchar NOT NULL
        );  
"""



# def selec_f():
#     conn.execute("SELECT * FROM train")
#     conn.commit()
#     return conn.execute("SELECT * FROM train").fetchall()


# print(selec_f())
# cursor.execute(create_table_query)
cursor.execute(create_table_passengers)
cursor.execute(create_table_reserve)


conn.commit()
conn.close()
