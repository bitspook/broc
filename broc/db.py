import sqlite3
from datetime import datetime

import broc

def create_db_if_not_exists(cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS income
    (id INTEGER PRIMARY KEY,
    repository TEXT,
    commit_hash TEXT,
    commit_message TEXT,
    points_earned INTEGER,
    created_at TEXT,
    author_email TEXT,
    author_name TEXT
    )
    """)

    cursor.execute("""CREATE TABLE IF NOT EXISTS expense
    (id INTEGER PRIMARY KEY,
    reason TEXT,
    points_spent Integer,
    created_at TEXT
    )
    """)


def add_commit_entry(repo, hash, msg, points_earned, created_at, author_name, author_email):
    conn = sqlite3.connect(broc.BROC_ROOT_DIR + "/broc.db")
    cursor = conn.cursor()

    create_db_if_not_exists(cursor)
    query = "INSERT INTO income (repository, commit_hash, commit_message, points_earned, created_at, author_email, author_name) VALUES (?, ?, ?, ?, ?, ?, ?)"

    cursor.execute(query, (repo, hash, msg, points_earned, created_at, author_name, author_email, ))
    conn.commit()
    conn.close()
