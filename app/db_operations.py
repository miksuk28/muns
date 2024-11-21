class Users:
    CREATE_USER = '''
        INSERT INTO users (id, username)
        VALUES (:id, :username)
    '''

    NEW_EXPENSE = '''
        INSERT INTO expenses (id)
        VALUES (id)
    '''