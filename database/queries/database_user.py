from database import database_connection

@database_connection.connection_handler
def select_user_by_username(cursor, username):
    cursor.execute("""
                    SELECT id, creation_date, username, password
                    FROM users
                    WHERE username = %(username)s     
                    """,
                   {'username': username})

    user = cursor.fetchone()
    return user