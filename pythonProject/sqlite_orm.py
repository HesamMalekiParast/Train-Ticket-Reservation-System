import sqlite3
from datetime import datetime

# Database connection setup
DB_FILE = 'train.db'


def connect_db():
    """
    Connect to the SQLite database and return the connection and cursor.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    return conn, cursor


def close_db(conn):
    """
    Close the database connection.
    """
    conn.close()

class Train:

    @staticmethod
    def view_all_trains():
        """
        Retrieve all available trains using a raw SQL query.
        """
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
        """
        Search for trains by destination and departure date.

        :param destination: The destination city to search for.
        :param departure_date: The exact date and time (string in 'YYYY-MM-DD HH:MM:SS' format) of departure.
        :return: List of matching trains.
        """
        conn, cursor = connect_db()

        try:
            # Convert departure_date to the standard datetime format
            departure_datetime = datetime.strptime(departure_date, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            print("Invalid date format. Please use 'YYYY-MM-DD HH:MM:SS'")
            close_db(conn)
            return []

        # SQL query with parameters to filter by destination and departure_time
        query = """
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