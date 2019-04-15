from database import database_connection


@database_connection.connection_handler
def get_just_shows(cursor):
    cursor.execute("""
            SELECT id, title FROM shows  
    """),
    shows = cursor.fetchall()
    return shows


@database_connection.connection_handler
def check_id_exists_in_database(cursor, showId):
    cursor.execute("""
                SELECT * from shows
                WHERE id = %(showId)s """,

                   {'showId':showId})
    show = cursor.fetchone()
    return show