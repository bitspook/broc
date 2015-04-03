import sqlite3
from datetime import datetime
from calendar import timegm

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
    created_at TEXT,
    author_email TEXT
    )
    """)


def db_operation(func):
    """Decorator for functions who need a cursor and connection and close them after work"""
    def wrapper(*args):
        conn = sqlite3.connect(broc.BROC_ROOT_DIR + "/broc.db")
        cursor = conn.cursor()
        create_db_if_not_exists(cursor)

        return func(*args, conn=conn, cursor=cursor)
    return wrapper

@db_operation
def add_commit_entry(repo, hash, msg, points_earned, created_at, author_name, author_email, conn, cursor):
    query = "INSERT INTO income (repository, commit_hash, commit_message, points_earned, created_at, author_email, author_name) VALUES (?, ?, ?, ?, ?, ?, ?)"

    cursor.execute(query, (repo, hash, msg, points_earned, created_at, author_email, author_name, ))
    conn.commit()
    conn.close()

@db_operation
def add_spend_entry(points_spent, message, email, conn, cursor):
    created_at = datetime.now()

    query = "INSERT INTO expense (points_spent, reason, created_at, author_email) VALUES (?, ?, ?, ?)"

    cursor.execute(query, (points_spent, message, created_at, email))
    conn.commit()
    conn.close()

@db_operation
def get_total_brownie_points(email, conn, cursor):
    """Get total brownie points remaining in the account at the moment"""
    total_income = cursor.execute('SELECT sum(points_earned) FROM income WHERE author_email = ?', (email,)).fetchall()[0][0] or 0
    total_expenditure = cursor.execute('SELECT sum(points_spent) FROM expense WHERE author_email = ?', (email,)).fetchall()[0][0] or 0

    balance = total_income - total_expenditure

    conn.commit()
    conn.close()

    return balance

@db_operation
def get_todays_stats(email, conn, cursor):
    income = cursor.execute("SELECT sum(points_earned) FROM income WHERE created_at >= date('now') and author_email = ?", (email, )).fetchall()[0][0] or 0
    expenditure = cursor.execute("SELECT sum(points_spent) FROM expense WHERE created_at >= date('now') and author_email = ?", (email, )).fetchall()[0][0] or 0

    conn.commit()
    conn.close()

    return (income, expenditure, )
