import sqlite3

DB_NAME = "memvault.db"

def init_db():

    conn = sqlite3.connect(DB_NAME)

    # Memories table
    conn.execute("""
    CREATE TABLE IF NOT EXISTS memories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL,
        created_at TEXT NOT NULL
    )
    """)

    # Facts table
    conn.execute("""
    CREATE TABLE IF NOT EXISTS facts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        memory_id INTEGER,
        fact_type TEXT,
        fact_value TEXT
    )
    """)

    conn.commit()
    conn.close()