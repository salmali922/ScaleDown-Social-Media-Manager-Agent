import sqlite3
from datetime import datetime

scheduled_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def schedule_post(content, platform, time, score):
    conn = sqlite3.connect("posts.db")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO posts (content, platform, time, score) VALUES (?, ?, ?, ?)",
        (content, platform, time, score)
    )

    conn.commit()
    conn.close()
