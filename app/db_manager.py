import sqlite3
from contextlib import contextmanager
from config import config
from uuid import uuid4

class DatabaseConnection:
    def __init__(self):
        self._db_file = config["DB_FILE"]
        self._conn =    sqlite3.connect(self._db_file)


    def id(self):
        return str(uuid4())


    @contextmanager
    def cur(self, commit=True):
        _cur = self._conn.cursor()
        try:
            yield _cur
            if commit:
                self._conn.commit()

        except sqlite3.Error as e:
            self._conn.rollback()
            raise(e)

        finally:
            _cur.close()

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

    