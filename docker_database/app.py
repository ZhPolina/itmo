import time
import datetime

from flask import Flask

import sqlite3

import redis


app = Flask(__name__)
cache = redis.Redis(host='redishost', port=6379)

def get_hit_count():
    # подключение к базе данных
    conn = sqlite3.connect('count.db', check_same_thread=False)
    cur = conn.cursor()

    # создание таблицы, если такой не существует
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
        `count` INTEGER PRIMARY KEY AUTOINCREMENT,
        `datetime` timestamp
        );
        """)
    conn.commit()
    users = (datetime.datetime.now() + datetime.timedelta(hours=3)).strftime('%Y-%m-%d %H:%M:%S')
    cur.execute("INSERT INTO users(datetime) VALUES(?)", (users,))
    records = cur.execute("SELECT * FROM users ORDER BY COUNT DESC LIMIT 1;")
    records = cur.fetchall()
    conn.commit()
    conn.close()
    return records

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times '.format(count[0][0])+'last at: ' + count[0][1]