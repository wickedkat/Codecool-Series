from data import database_connection

@database_connection.connection_handler
def get_shows(cursor):
    cursor.execute("""
            SELECT id, title FROM shows  
    """),
    shows = cursor.fetchall()
    return shows

