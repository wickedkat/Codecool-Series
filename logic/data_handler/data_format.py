from datetime import datetime

from database.queries import database_shows

from logic.data_handler import data_validation


def format_actors_list(actors):
    actors_list = []
    for actor in actors:
        actors_list.append(actor['name'])
    return actors_list


def get_episodes_by_show_and_season(seasons):
    for season in seasons:
        seasonId = season['season_id']
        episodes = database_shows.get_episodes_by_show_and_season(seasonId)
        season['episodes'] = episodes
    return seasons


def get_show_by_id_from_database(showId):
    data_validation.check_id_exists_in_database(showId)
    show = database_shows.get_details_one_show(showId)
    return show


def get_actors_with_characters_from_database():
    actors = database_shows.get_all_actors()
    for actor in actors:
        characters = database_shows.get_shows_and_characters_by_actor_id(actor['id'])
        actor['roles'] = characters
        actor['roles_count'] = len(characters)
    return actors


def check_data_for_parenthesis(random_data):
    if random_data:
        if random_data[0] == '(' or random_data[0] == '[' or random_data[0] == '<':
            return random_data[1:]
        else:
            return random_data



