from db_manager import DatabaseConnection
from db_operations import Users     as sql_u
from db_operations import Expenses  as sql_e

class Expense(DatabaseConnection):
    def __init__(self, id):
        super().__init__()
        self.id = id
        #self._init()


    '''
    def _init(self):
        # if no expense id passed to class, create new expense
        if self.id is None:
            # random uuid
            self.id = self.genid()
            with self.cur() as cur:
                cur.execute(sql_e.NEW_EXPENSE, self.id)
                return

        with self.cur(commit=False) as cur:
            cur.execute()
    '''    

    def _get_items(self):
        with self.cur() as cur:
            cur.execute(sql_e.GET_ITEMS, (self.id,))
            self._items = cur.fetchall()


    def create_user(self, username):
        id = self.genid()
        with self.cur() as cur:
            cur.execute(sql_u.CREATE_USER,
                {"id": id,
                "username": username}
            )

            return id