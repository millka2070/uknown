#database
import sqlite3


def init_db():
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            name TEXT,
            age TEXT,
            about TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_anket(user_id, name, age, about):
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO users(user_id, name, age, about)
        VALUES (?, ?, ?, ?)
    ''', (user_id, name, age, about))
    conn.commit()
    conn.close()

def get_anket(user_id):
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result

