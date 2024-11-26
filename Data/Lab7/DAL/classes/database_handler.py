"""Handles the history functionality as a database"""
import csv
import json
import sqlite3


class DBHandler:
    """A history database handler class"""
    def __init__(self, db_name="Data/Lab7/DAL/assets/prompt_history.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """Creates the history table if not exists"""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            link TEXT NOT NULL,
            type TEXT NOT NULL CHECK(type IN ('GET', 'POST', 'PATCH', 'DELETE')),
            entity_id TEXT NOT NULL
        )
        """)
        self.connection.commit()

    def insert_history(self, link, request_type, entity_id):
        """Inserts a new history entry into the history table"""
        self.cursor.execute("""
        INSERT INTO history (link, type, entity_id) 
        VALUES (?, ?, ?)
        """, (link, request_type, entity_id))
        self.connection.commit()

    def fetch_history(self):
        """Fetches the history from the database"""
        self.cursor.execute("SELECT * FROM history")
        return self.cursor.fetchall()

    def export_to_txt(self, filename="history.txt"):
        """Exports the history to the txt file"""
        history = self.fetch_history()
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"{'ID':<5} {'Link':<20} {'Type':<10} {'Entity ID':<10}\n")
            file.write("=" * 50 + "\n")
            for row in history:
                file.write(f"{row[0]:<5} {row[1]:<20} {row[2]:<10} {row[3]:<10}\n")

    def export_to_csv(self, filename="history.csv"):
        """Exports the history to the csv file"""
        history = self.fetch_history()
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Link", "Type", "Entity ID"])
            writer.writerows(history)

    def export_to_json(self, filename="history.json"):
        """Exports the history to the json file"""
        history = self.fetch_history()
        data = [{"id": row[0], "link": row[1], "type": row[2],
                 "entity_id": row[3]} for row in history]
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def close(self):
        """Closes the connection to the database"""
        self.connection.close()
