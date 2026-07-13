# Repository for database operations related to careers.
import sqlite3

# Handles storing and retrieving career information.
class CareerRepository:
# Retrieve all careers from the database.
    def save_recommendation(self, username, career, score):

        conn = sqlite3.connect("data/careers.db")

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO recommendations(username, career, score)
            VALUES (?, ?, ?)
            """,
            (username, career, score)
        )

        conn.commit()
        conn.close()