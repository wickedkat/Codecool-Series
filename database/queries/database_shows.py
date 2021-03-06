from database import database_connection


@database_connection.connection_handler
def get_just_shows(cursor):
    cursor.execute("""
            SELECT id, title FROM shows  
    """),
    shows = cursor.fetchall()
    return shows


@database_connection.connection_handler
def get_all_genres(cursor):
    cursor.execute("""
            SELECT * from genres """),

    genres = cursor.fetchall()
    return genres


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
            array_agg(DISTINCT seasons.title) as seasons,
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
def get_details_one_show(cursor, showId):
    cursor.execute("""
            SELECT
            shows.title,
            to_char(year, 'YYYY') as year,
            to_char(runtime, '99') as runtime,
            to_char(rating, '9.99999') as rating,
            trailer,
            homepage,
            shows.overview,
            array_agg(DISTINCT genres.name) as genre,
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
def get_actors_by_show(cursor, showId):
    cursor.execute("""
            SELECT name
            FROM actors
            JOIN show_characters sc on actors.id = sc.actor_id
            JOIN shows  on sc.show_id = shows.id
            WHERE shows.id = %(showId)s
            """,
                   {'showId': showId})
    actors = cursor.fetchall()
    return actors


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
def get_show_title_by_id(cursor, showId):
    cursor.execute("""
            SELECT title from shows
            WHERE id = %(showId)s
            """,
                   {'showId': showId})

    title = cursor.fetchone()
    return title


@database_connection.connection_handler
def get_episodes_by_show_and_season(cursor, season_id):
    cursor.execute("""
            SELECT 
                seasons.title as season_title,
                to_char(episode_number, '999') as episode_number,
                episodes.title as episode_title,
                episodes.overview as episode_overview
                FROM episodes
                LEFT JOIN seasons  on episodes.season_id = seasons.id
                JOIN shows  on seasons.show_id = shows.id
                WHERE seasons.id = %(season_id)s          
    """,

                   {'season_id': season_id}),

    episodes = cursor.fetchall()
    return episodes


@database_connection.connection_handler
def check_id_exists_in_database(cursor, showId):
    cursor.execute("""
                SELECT * from shows
                WHERE id = %(showId)s """,

                   {'showId': showId})
    show = cursor.fetchone()
    return show


@database_connection.connection_handler
def get_all_actors(cursor):
    cursor.execute("""
            SELECT id,
            name,
            COALESCE(to_char(birthday, 'DD/MM/YYYY'), 'no data') as birthday,
            COALESCE(to_char(death, 'DD/MM/YYYY'), 'alive') as death,
            biography
            from actors
            LIMIT 20
            
            """)

    actors = cursor.fetchall()
    return actors


@database_connection.connection_handler
def get_shows_and_characters_by_actor_id(cursor, actorId):
    cursor.execute("""
            SELECT
            character_name,
            shows.title,
            shows.overview,
            shows.id
            from shows
            RIGHT JOIN  show_characters s on shows.id = s.show_id
            JOIN actors a on s.actor_id = a.id
            WHERE actor_id = %(actorId)s
            """,
                   {'actorId': actorId})

    characters = cursor.fetchall()
    return characters


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
def add_new_actor_to_database(cursor, actor):
    cursor.execute("""
                   INSERT INTO actors (name, birthday, death,  biography)
                   VALUES (%(name)s, %(birthday)s, %(death)s,  %(biography)s)
                   """,
                   {'name': actor['name'],
                    'birthday': actor['birthday'],
                    'death': actor['death'],
                    'biography': actor['biography']})


@database_connection.connection_handler
def check_actor_exists_in_database(cursor, actor):
    cursor.execute("""
    SELECT * from actors 
    WHERE name = %(name)s 
    AND birthday = %(birthday)s  
    """,
                   {'name': actor['name'],
                    'birthday': actor['birthday']})

    actor = cursor.fetchone()
    return actor


@database_connection.connection_handler
def get_actors_played_more_than_X_shows(cursor, min):
    cursor.execute("""
            SELECT actors.name,
            string_agg(DISTINCT title, ', ') as shows
            FROM actors
            LEFT JOIN show_characters sc on actors.id = sc.actor_id
            JOIN shows s on sc.show_id = s.id
            GROUP BY actors.name
            HAVING COUNT(actor_id) >= %(min)s 
            """,
                   {'min':min})

    actors = cursor.fetchall()
    return actors
