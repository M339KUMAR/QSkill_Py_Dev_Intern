import sqlite3

DB_NAME = "database/chatbot.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def initialize_database():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT,

            created_at TEXT

        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            conversation_id INTEGER,

            role TEXT,

            content TEXT,

            timestamp TEXT

        )
    """)

    conn.commit()

    conn.close()
