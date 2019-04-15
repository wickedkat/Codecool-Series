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

                   {'showId': showId})
    show = cursor.fetchone()
    return show


@database_connection.connection_handler
def get_all_genres(cursor):
    cursor.execute("""
            SELECT * from genres """),

    genres = cursor.fetchall()
    return genres


@database_connection.connection_handler
def get_shows_by_genre(cursor, genre):
    cursor.execute("""
        SELECT title,
        to_char(year, 'YYYY') as year,
        to_char(rating, '9.99999') as rating
        from shows
        JOIN show_genres sg on shows.id = sg.show_id
        JOIN genres g on sg.genre_id = g.id
        WHERE g.name = %(genre)s
        ORDER BY rating DESC
        """,
                   {'genre': genre})

    shows = cursor.fetchall()
    return shows
