import sqlite3


class DataBase:

    def __init__(self, db_path: str = 'Database/bot_db.db'):
        self.db_path = db_path

    @property
    def connection(self):
        return sqlite3.connect(self.db_path)

    def execute(self, sql: str, parameters: tuple = tuple(),
                fetchone=False, fetchall=False, commit=False):
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS users 
        (user_id INTEGER PRIMARY KEY,
        tg_id INTEGER, count INTEGER, turn INTEGER, poster TEXT)'''
        self.execute(sql, commit=True)

    def new_user(self, tg_id: int):
        sql = 'SELECT * FROM users WHERE tg_id=?'
        user = self.execute(sql, (tg_id,), fetchone=True)
        if not user:
            sql = 'INSERT INTO users (tg_id, count, turn) VALUES (?, ?, ?)'
            self.execute(sql, (tg_id, 300, 28), commit=True)

    def me(self, tg_id: int):
        sql = 'SELECT count, turn FROM users WHERE tg_id=?'
        return self.execute(sql, (tg_id,), fetchone=True)

    def poster(self, tg_id: int, url_poster: str = ''):
        if url_poster:
            sql = 'UPDATE users SET poster=? WHERE tg_id=?'
            self.execute(sql, (url_poster, tg_id), commit=True)
        sql = 'SELECT poster FROM users WHERE tg_id=?'
        return self.execute(sql, (tg_id,), fetchone=True)

    def setup(self, tg_id: int, target: str, count: int):
        sql = f'UPDATE users SET {target}=? WHERE tg_id=?'
        self.execute(sql, (count, tg_id), commit=True)

    @staticmethod
    def extract_kwargs(sql: str, parameters: dict) -> tuple:
        sql += ' AND '.join([f'{key} = ?' for key in parameters])
        return sql, tuple(parameters.values())

    def disconnect(self):
        self.connection.close()
