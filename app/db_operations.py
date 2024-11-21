class Users:
    CREATE_USER = '''
        INSERT INTO users (id, username)
        VALUES (:id, :username)
    '''

    NEW_EXPENSE = '''
        INSERT INTO expenses (id)
        VALUES (id)
    '''

    GET_ITEMS = '''
        SELECT i.name AS item, i.price, u.id AS userId, u.username
        FROM items i
        LEFT JOIN users u ON i.costBearerId = u.id
        WHERE expenseId=?
    '''