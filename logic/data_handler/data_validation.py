from database.queries import database_shows
from logic.data_handler import data_format


class InvalidData(Exception):
    pass


class InvalidFormat(Exception):
    pass


class DoubledData(Exception):
    pass


def check_empty_list(random_list):
    if random_list:
        return random_list
    else:
        raise InvalidData


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


def validate_show_details(show_id):
    show_db = data_format.get_show_by_id_from_database(show_id)
    show = check_empty_list(show_db)
    return show


def validate_actors_by_showid(showId):
    actors_dict = database_shows.get_actors_by_show(showId)
    actors_list = data_format.format_actors_list(actors_dict)
    actors = check_empty_list(actors_list)
    return actors


def validate_seasons_by_showId(showId):
    seasons_db = database_shows.get_seasons_by_show(showId)
    seasons = check_empty_list(seasons_db)
    return seasons


def validate_show_title(showId):
    title_db = database_shows.get_show_title_by_id(showId)
    title = check_empty_list(title_db)
    return title


def validate_episodes_by_show_and_seasons(seasons):
    seasons_episodes_db = data_format.get_episodes_by_show_and_season(seasons)
    seasons_episodes = check_empty_list(seasons_episodes_db)
    return seasons_episodes


def validate_actors_list():
    actors_db = data_format.get_actors_with_characters_from_database()
    actors = check_empty_list(actors_db)
    return actors


def check_new_actor_exists_in_database(actor):
    actor_in_db = database_shows.check_actor_exists_in_database(actor)
    if actor_in_db:
        raise DoubledData
    else:
        database_shows.add_new_actor_to_database(actor)


def validate_new_actor(actor):
    actor['name'] = data_format.check_data_for_parenthesis(actor['name'])
    actor['birthday'] = data_format.check_data_for_parenthesis(actor['birthday'])
    actor['death'] = data_format.check_data_for_parenthesis(actor['death'])
    actor['biography'] = data_format.check_data_for_parenthesis(actor['biography'])
    check_new_actor_exists_in_database(actor)

def validate_min_parameter(min):
    check_datatype_integer(min)
    actors = database_shows.get_actors_played_more_than_X_shows(min)
    return actors

