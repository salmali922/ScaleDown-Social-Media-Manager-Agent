import sqlite3

conn = sqlite3.connect("posts.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY,
    content TEXT,
    platform TEXT,
    time TEXT,
    score INTEGER
)
""")

conn.commit()
