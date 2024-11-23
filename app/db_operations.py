class Users:
    CREATE_USER = '''
        INSERT INTO users (id, username)
        VALUES (:id, :username)
    '''

    GET_USER = '''
        SELECT username
        FROM users
        WHERE id=?
    '''

    QUERY_USERS = '''
        SELECT id, username
        FROM users
        WHERE username LIKE ?
        OR
        id=?
    '''


class Expenses:
    GET_ITEMS = '''
        SELECT i.name AS item, i.price, u.id AS userId, u.username
        FROM items i
        LEFT JOIN users u ON i.costBearerId = u.id
        WHERE expenseId=?
    '''

    NEW_EXPENSE = '''
        INSERT INTO expenses (id)
        VALUES (id)
    '''