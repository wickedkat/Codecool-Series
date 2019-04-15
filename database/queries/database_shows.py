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

@database_connection.connection_handler
def get_all_shows(cursor):
    cursor.execute("""
            SELECT 
            shows.id,
            shows.title, 
            to_char(year, 'YYYY') as year, 
            to_char(runtime, '99') as runtime,
            to_char(rating, '9.99999') as rating, 
            trailer, 
            homepage, 
            array_agg(DISTINCT name) as genre,
            array_agg(DISTINCT seasons.title) as seasons_titles,
            shows.id as id
            from shows
            LEFT JOIN show_genres on shows.id = show_genres.show_id
            LEFT JOIN genres on show_genres.genre_id = genres.id
            LEFT JOIN seasons on shows.id = seasons.show_id
            GROUP BY shows.title, shows.year, shows.runtime,
            shows.rating, shows.trailer, shows.homepage, shows.id
            ORDER BY rating DESC            
            """),
    shows = cursor.fetchall()
    return shows

@database_connection.connection_handler
def get_seasons_by_show(cursor, showId):
    cursor.execute("""
            SELECT shows.id  as show_id,
            seasons.id as season_id,
            to_char(season_number, '99') as season_number,
            seasons.title,
            seasons.overview,
            COUNT(DISTINCT episode_number) as episodes_count
            FROM shows
            LEFT JOIN seasons on shows.id = seasons.show_id
            JOIN episodes e on seasons.id = e.season_id
            WHERE shows.id = %(showId)s
            GROUP BY  shows.id, shows.title, seasons.id, seasons.season_number,
            seasons.title, seasons.overview
        
            """,
                   {'showId': showId}),

    seasons = cursor.fetchall()
    return seasons


