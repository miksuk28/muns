import sqlite3
from contextlib import contextmanager
from config import config

class DatabaseConnection:
    def __init__(self):
        self._db_file = config["DB_FILE"]
        self._conn =    sqlite3.connect(self._db_file)

'''
    @contextmanager
    def cur(self, stmt, params=None, fetchone=False, commit=True):
        _cur = self._conn.cursor()
        try:
            _cur.execute(stmt, params)
            if commit:
                self._conn.commit()

        except Error as e:
            self._conn.rollback()
            raise(e)

        finally:
            _cur.close()
'''