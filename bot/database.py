import sqlite3
from datetime import datetime

conn = sqlite3.connect('telegram_bot.db')  # Создание файла базы данных
cursor = conn.cursor()  # Создание объекта курсора

# Создание таблицы
cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY,
        chanel_id INTEGER,
        main_text TEXT,
        link TEXT,
        media TEXT, 
        url_name TEXT,
        message_id INTEGER,
        ch_message_id INTEGER,
        date DATETIME
    )
''')
cursor.execute('''

CREATE TABLE IF NOT EXISTS chanels (
    sid INTEGER PRIMARY KEY,
    id INTEGER,
    tg_id INTEGER, 
    name TEXT
    )
    ''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS templates (
    id INTEGER PRIMARY KEY,
    chanel_id INTEGER,
    text TEXT,
    media TEXT,
    url_name TEXT,
    link TEXT
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS content (
    id INTEGER PRIMARY KEY,
    title TEXT,
    send_time DATETIME
)
''')
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT, subscription BOOLEAN)')


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('telegram_bot.db')
        self.cursor = self.connection.cursor()

    def add_user(self, user_id, name):
        with self.connection:
            return self.cursor.execute("INSERT INTO users VALUES (?, ?, ?)", (user_id, name, True))

    def get_user_subscription(self, user_id):
        with self.connection:
            data = self.cursor.execute("SELECT subscription FROM users WHERE id = ?", (user_id,)).fetchone()
            if data:
                return data[0]
            else:
                return None

    def delete_chanel(self, ch_id):
        with self.connection:
            return self.cursor.execute("DELETE FROM chanels WHERE id = ?", (ch_id,))

    def add_chanel_id(self, ch_id, user_id, title):
        with self.connection:
            return self.cursor.execute("INSERT INTO chanels (id, tg_id, name) VALUES (?, ?, ?)",
                                       (ch_id, user_id, title))

    def get_chanel_id(self, user_id):
        with self.connection:
            data = self.cursor.execute("SELECT id FROM chanels WHERE tg_id = ?", (user_id,)).fetchone()
            if data:
                return data[0]
            else:
                return None

    def get_chanel_name(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT name FROM chanels WHERE tg_id = ?",
                                         (user_id,)).fetchone()

            if result:
                return result[0]
            else:
                return None

    def get_all_chanels_name_ch_id_from_user_id(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT name, id FROM chanels WHERE tg_id = ?", (user_id,)).fetchall()

    def get_all_chanels_name_from_user_id(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT name FROM chanels WHERE tg_id = ?", (user_id,)).fetchall()

    def get_all_chanels_id_from_user_id(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT id FROM chanels WHERE tg_id = ?", (user_id,)).fetchall()

    def get_post(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM posts").fetchall()

    def add_post_text(self, ch_id, main_text, message_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO posts (chanel_id, main_text, message_id, date) VALUES (?, ?, ?, ?)",
                                       (ch_id, main_text, message_id, datetime.now()))

    def add_post_link(self, ch_id, url_name, link, message_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO posts (chanel_id, url_name, link, message_id) VALUES (?, ?, ?, ?)",
                                       (ch_id, url_name, link, message_id))

    def add_post_media(self, ch_id, media, message_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO posts (chanel_id, media, message_id) VALUES (?, ?, ?)",
                                       (ch_id, media, message_id))

    def add_post_all(self, ch_id, main_text, link, media, url_name, message_id, ch_message_id=None):
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO posts (chanel_id, main_text, link, media, url_name, date, message_id, ch_message_id) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (ch_id, main_text, link, media, url_name, datetime.now(), message_id, ch_message_id))

    def delete_post(self, message_id):
        with self.connection:
            return self.cursor.execute("DELETE FROM posts WHERE message_id = ?", (message_id,))

    def update_text(self, message_id, new_text):
        with self.connection:
            return self.cursor.execute("UPDATE posts SET main_text = ? WHERE message_id = ?", (new_text, message_id))

    def update_link(self, message_id, new_link):
        with self.connection:
            return self.cursor.execute("UPDATE posts SET link = ?WHERE message_id = ?", (new_link, message_id))

    def update_url_name(self, message_id, new_url_name):
        with self.connection:
            return self.cursor.execute("UPDATE posts SET url_name = ? WHERE message_id = ?", (new_url_name, message_id))

    def update_media(self, message_id, new_media):
        with self.connection:
            return self.cursor.execute("UPDATE posts SET media = ? WHERE message_id = ?", (new_media, message_id))

    def get_all_posts(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM posts").fetchall()

    def get_post_text(self, message_id):
        with self.connection:
            data = self.cursor.execute("SELECT main_text FROM posts WHERE message_id = ?", (message_id,)).fetchone()
            if data:
                return data[0]
            else:
                return None

    def get_post_media(self, message_id):
        with self.connection:
            data = self.cursor.execute("SELECT media FROM posts WHERE message_id = ?", (message_id,)).fetchone()
            if data:
                return data[0]
            else:
                return None

    # def delete_post_media

    def get_post_url_name(self, message_id):
        with self.connection:
            data = self.cursor.execute("SELECT url_name FROM posts WHERE message_id = ?", (message_id,)).fetchone()
            if data:
                return data[0]
            else:
                return None

    def get_post_url(self, message_id):
        with self.connection:
            data = self.cursor.execute("SELECT link FROM posts WHERE message_id = ?", (message_id,)).fetchone()

            if data:
                return data[0]
            else:
                return None

    def delete_all_post(self):
        with self.connection:
            return self.cursor.execute("DELETE FROM posts")

    def delete_post_photo(self, message_id):
        with self.connection:
            return self.cursor.execute("UPDATE posts SET media = NULL WHERE message_id = ?", (message_id,))

    def update_message_id(self, message_id, new_message_id):
        with self.connection:
            return self.cursor.execute("UPDATE posts SET message_id = ? WHERE message_id = ?",
                                       (new_message_id, message_id))

    def update_template_text(self, ch_id, text):
        with self.connection:
            return self.cursor.execute("UPDATE templates SET text = ? WHERE chanel_id = ?", (text, ch_id))

    def update_template_media(self, ch_id, media):
        with self.connection:
            return self.cursor.execute("UPDATE templates SET media = ? WHERE chanel_id = ?", (media, ch_id))

    def update_template_url_name(self, ch_id, url_name):
        with self.connection:
            return self.cursor.execute("UPDATE templates SET url_name = ? WHERE chanel_id = ?", (url_name, ch_id))

    def update_template_link(self, ch_id, link):
        with self.connection:
            return self.cursor.execute("UPDATE templates SET link = ? WHERE chanel_id = ?", (link, ch_id))

    def get_all_template_post(self, ch_id):
        with self.connection:
            return self.cursor.execute("SELECT * FROM templates WHERE chanel_id = ?", (ch_id,)).fetchall()

    def add_template(self, ch_id, text):
        with self.connection:
            return self.cursor.execute("INSERT INTO templates (chanel_id, text) VALUES (?, ?)",
                                       (ch_id, text))

    def delete_template_post(self, ch_id, text):
        with self.connection:
            return self.cursor.execute("DELETE FROM templates WHERE chanel_id = ? AND text = ?", (ch_id, text))

    def add_content(self, title, time):
        with self.connection:
            return self.cursor.execute("INSERT INTO content (title, send_time) VALUES (?, ?)",
                                       (title, time))

    def get_all_content(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM content").fetchall()
