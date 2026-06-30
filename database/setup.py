import sqlite3


def create_tables():

    conn = sqlite3.connect("data/careers.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS recommendations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        career TEXT,
        score INTEGER
    )
    """)

    conn.commit()
    conn.close()