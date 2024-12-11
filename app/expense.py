from db_manager import DatabaseConnection
from db_operations import Expenses  as sql_e

class Expense(DatabaseConnection):
    def __init__(self, id=None):
        super().__init__()
        self.id = id
        #self._init()


    def _get_items(self):
        with self.cur() as cur:
            cur.execute(sql_e.GET_ITEMS, (self.id,))
            self._items = cur.fetchall()


    def add_item(self, user_id, name, price):
        with self.cur() as cur:
            



    def delete(self):
        if self.id is not None:
            with self.cur() as cur:
                cur.execute(sql_e.DELETE_EXPENSE, (self.id,))
                self.id = None


    @staticmethod
    def new():
        exp = Expense()
        id = exp.genid()
        with exp.cur() as cur:
            cur.execute(sql_e.NEW_EXPENSE, (id,))
            return Expense(id)