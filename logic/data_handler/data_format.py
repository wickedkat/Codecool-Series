from database.queries import database_shows

from logic.data_handler import data_validation

def get_episodes_by_show_and_season(seasons):  #function adding object['episodes'] within season objects
    for season in seasons:
        seasonId = season['season_id']
        episodes = database_shows.get_episodes_by_show_and_season(seasonId)
        season['episodes'] = episodes
    return seasons


