from db_manager import DatabaseConnection

class Expense(DatabaseConnection):
    def __init__(self):
        super().__init__()