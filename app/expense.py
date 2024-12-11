from db_manager import DatabaseConnection
from db_operations import Expenses  as sql_e

### CUSTOM EXCEPTIONS - MOVE TO SEPARATE FILE IN THE FUTURE ###
class UserNotFound(Exception):
    """Exception raised when user is not found by name or id

    Attributes:
        user_id - user id which was not found
        suername - username which was not found
    """

    def __init__(self, id=None, username=None, message="User cannot be found in database"):
        self.id = id
        self.username = username
        super().__init__(self.message)

### END CUSTOM EXCEPTIONS ###


class Expense(DatabaseConnection):
    def __init__(self, id=None):
        super().__init__()
        self.id = id
        #self._init()

    
    def _get_user_id(self, username):
        '''get user_id by username, raise UserNotFound if not found'''
        with self.cur() as cur:
            cur.execute(sql_e.GET_USER_ID, (username))
            user_id = cur.fetchone()

            if user_id is None:
                raise UserNotFound(username)
            
            return user_id["id"]


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