import sqlite3
from datetime import datetime

DB = "logs.db"


def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            status TEXT,
            created_at TEXT
        )
        """
    )

    conn.commit()
    conn.close()


def save_log(status):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO logs(status, created_at) VALUES (?, ?)",
        (status, datetime.now().isoformat()),
    )

    conn.commit()
    conn.close()


def get_logs(limit=10):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute(
        "SELECT status, created_at FROM logs ORDER BY id DESC LIMIT ?",
        (limit,),
    )

    rows = cur.fetchall()
    conn.close()

    return rows
