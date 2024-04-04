import sqlite3
# from datetime import datetime
#
# now = datetime.now()
class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        with self.connection:
            self.cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,'
                                ' username TEXT, email TEXT, password TEXT, time TEXT)')
            return

    def user_exists(self, username):
        with self.connection:
            result = self.cursor.execute(f"SELECT id FROM users WHERE username = '{username}'").fetchone()
            if not result:
                return False
            else:
                return True

    def add_new_user(self, username, email, password, timestamp):
        with self.connection:
            self.cursor.execute(f"INSERT INTO users (username, email, password, time) VALUES ('{username}', '{email}', '{password}', '{timestamp}')")
            return

    def user_login(self, username_email, password):
        with self.connection:
            success = False
            login_username = self.cursor.execute(f"SELECT id FROM users WHERE username = '{username_email}' AND password = '{password}'").fetchone()
            if login_username:
                success = True
                return success
            else:
                login_email = self.cursor.execute(f"SELECT id FROM users WHERE email = '{username_email}' AND password = '{password}'").fetchone()
                if login_email:
                    success = True
                    return success
                else:
                    print(success)
                    return success
