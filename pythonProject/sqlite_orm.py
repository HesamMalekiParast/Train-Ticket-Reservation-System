import sqlite3
from datetime import datetime

# Database connection setup
DB_FILE = 'train.db'


def connect_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    return conn, cursor


def close_db(conn):
    conn.close()

class Train:

    @staticmethod
    def view_all_trains():
        conn, cursor = connect_db()

        # Raw SQL query to select all trains
        cursor.execute("SELECT * FROM trains")
        trains = cursor.fetchall()

        # Display results
        for train in trains:
            print(train)

        close_db(conn)
        return trains

    @staticmethod
    def search_trains(destination, departure_date):
        conn, cursor = connect_db()

        try:
            # Convert departure_date to the standard datetime format
            departure_datetime = datetime.strptime(departure_date, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            print("Invalid date format. Please use 'YYYY-MM-DD HH:MM:SS'")
            close_db(conn)
            return []

        # SQL query with parameters to filter by destination and departure_time
        query = f"""
        SELECT * FROM trains
        WHERE destination = ? AND departure_time = ?
        """
        cursor.execute(query, (destination, departure_datetime.strftime('%Y-%m-%d %H:%M:%S')))
        trains = cursor.fetchall()

        # Display results
        for train in trains:
            print(train)

        close_db(conn)
        return trains


# Usage example
print("All available trains:")
train_obj = Train()
train_obj.view_all_trains()

print("\nSearching for trains to 'New York' on '2024-12-01 08:00:00'")
train_obj.search_trains("New York", "2024-12-01 08:00:00")