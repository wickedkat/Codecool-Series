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


@database_connection.connection_handler
def get_episodes_by_show_and_season(cursor, season_id):
    cursor.execute("""
            SELECT 
                seasons.title as season_title,
                seasons.id as season_id,
                episodes.id as episode_id,
                to_char(episode_number, '999') as episode_number,
                episodes.title as episode_title,
                episodes.overview as episode_overview,
                shows.title as show_title,
                shows.id as show_id
                FROM episodes
                LEFT JOIN seasons  on episodes.season_id = seasons.id
                JOIN shows  on seasons.show_id = shows.id
                WHERE seasons.id = %(season_id)s          
    """,

                   {'season_id': season_id}),

    episodes = cursor.fetchall()
    return episodes


@database_connection.connection_handler
def get_show_by_id(cursor, showId):
    cursor.execute("""
            SELECT
            shows.title,
            to_char(year, 'YYYY') as year,
            to_char(runtime, '99') as runtime,
            to_char(rating, '9.99999') as rating,
            trailer,
            homepage,
            shows.overview,
            string_agg(DISTINCT genres.name, ',') as genre,
            array_agg(DISTINCT seasons.title) as seasons,
            to_char(shows.id, '999999') as id
            from shows
            LEFT JOIN show_genres on shows.id = show_genres.show_id
            LEFT JOIN genres on show_genres.genre_id = genres.id
            LEFT JOIN seasons on shows.id = seasons.show_id
            WHERE shows.id = %(showId)s
            GROUP BY shows.title, shows.year, shows.runtime,
            shows.rating, shows.trailer, shows.homepage, shows.id
            """,
                   {'showId': showId})

    show = cursor.fetchone()
    return show

@database_connection.connection_handler
def get_show_by_season_id(cursor, seasonID):
    cursor.execute("""
            SELECT shows.id,
            shows.title,
            s.id as season_id
            from shows   
            JOIN seasons s on shows.id = s.show_id
            WHERE s.id = %(seasonID)s
    
    """,
                   {'seasonID':seasonID})

    show = cursor.fetchone()
    return show



