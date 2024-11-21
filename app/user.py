from db_manager import DatabaseConnection
from db_operations import Users as sql_u

class User(DatabaseConnection):
    def __init__(self, id=None):
        super().__init__()
        self.id = id
        self.username = None
        self._load_user()


    def _load_user(self):
        if self.id is not None:
            with self.cur() as cur:
                cur.execute(sql_u.GET_USER, (self.id,))
                res = cur.fetchone()

                if res:
                    self.username = res["username"]


    @staticmethod
    def new(username):
        user = User()
        id = user.genid()
        with user.cur() as cur:
            cur.execute(sql_u.CREATE_USER,
                {"id": id,
                "username": username}
            )

        return User(id)


    @staticmethod
    def query_users(username):
        with self.cur(commit=False) as cur:
            cur.execute(sql_u.QUERY_USERS, (username,))
