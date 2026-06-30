import sqlite3


class CareerRepository:

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