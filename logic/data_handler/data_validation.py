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


