from db_manager import DatabaseConnection
from db_operations import Users as sql
from uuid import uuid4

class Expense(DatabaseConnection, id=None):
    def __init__(self):
        super().__init__()
        self.id = id
        self._init()


    def _init(self):
        # if no expense id passed to class, create new expense
        if self.id is None:
            # random uuid
            self.id = self.id()
            with self.cur() as cur:
                cur.execute(sql.NEW_EXPENSE, self.id)
                return
        


    def create_user(self, username):
        id = self.id()
        with self.cur() as cur:
            cur.execute(sql.CREATE_USER,
                {"id": id,
                "username": username}
            )

            return id