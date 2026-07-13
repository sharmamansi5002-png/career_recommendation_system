# Database connection utility.
import sqlite3

# Create and return a connection to the SQLite database.
def get_connection():
    return sqlite3.connect("data/careers.db")
