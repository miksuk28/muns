from db_manager import DatabaseConnection
from db_operations import Expenses  as sql_e
import sqlite3

### CUSTOM EXCEPTIONS - MOVE TO SEPARATE FILE IN THE FUTURE ###
class UserNotFound(Exception):
    """Exception raised when user is not found by name or id

    Attributes:
        user_id - user id which was not found
        username - username which was not found
    """

    def __init__(self, id=None, username=None, message="User cannot be found in database"):
        self.id =       id
        self.username = username
        self.message =  message
        super().__init__(self.message)


class DuplicateItem(Exception):
    """Raised when an item with the same name for the user already exists
    
    Attributes:
        user_id -   Affected user ID
        name    -   Name of the conflicting item
        expense_id - Affected expense ID
    """

    def __init__(self, user_id=None, name=None, expense_id=None,message="Item already added on this expense for the respective user"):
        self.user_id =      user_id,
        self.name    =      name,
        self.expense_id =   expense_id,
        self.message =      message
### END CUSTOM EXCEPTIONS ###


class Expense(DatabaseConnection):
    def __init__(self, id=None):
        super().__init__()
        self.id = id
        #self._init()

    
    def _get_user_id(self, username):
        '''get user_id by username, raise UserNotFound if not found'''
        with self.cur() as cur:
            cur.execute(sql_e.GET_USER_ID, (username,))
            user_id = cur.fetchone()

            if user_id is None:
                raise UserNotFound(username)
            
            return user_id["id"]


    def _get_items(self):
        with self.cur() as cur:
            cur.execute(sql_e.GET_ITEMS, (self.id,))
            self._items = cur.fetchall()


    def add_item(self, username, name, price):
        user_id = self._get_user_id(username)
        item_id = self.genid()
        try:
            with self.cur() as cur:
                cur.execute(sql_e.ADD_ITEM, {
                    "id":            item_id,
                    "expenseId":     self.id,
                    "costBearerId":  user_id,
                    "name":          name,
                    "price":         price
                })
        
        except sqlite3.IntegrityError:
            # Raised if user already has an item with
            # the same name for this expense_id
            raise DuplicateItem(
                user_id=user_id,
                name=name
            )
        
        return item_id



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