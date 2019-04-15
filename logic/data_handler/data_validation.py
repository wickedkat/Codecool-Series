from database.queries import database_shows


class InvalidData(Exception):
    pass


class InvalidFormat(Exception):
    pass


def check_empty_list(random_list):
    if random_list:
        return random_list


def check_id_exists_in_database(showId):
    exists = database_shows.check_id_exists_in_database(showId)
    if exists:
        return True
    else:
        raise InvalidData


def check_datatype_integer(data):
    try:
        data = int(data)
        return data
    except Exception as e:
        print(e)
        raise InvalidFormat


def validate_genres_list():
    genres_db = database_shows.get_all_genres()
    genres = check_empty_list(genres_db)
    return genres

def validate_shows_by_genres_list(genre):
    shows_by_genres_db = database_shows.get_shows_by_genre(genre)
    shows_by_genres = check_empty_list(shows_by_genres_db)
    return shows_by_genres

def validate_shows():
    shows_db = database_shows.get_all_shows()
    shows = check_empty_list(shows_db)
    return shows