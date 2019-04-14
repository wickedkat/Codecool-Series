from flask import Flask, render_template, json, session, redirect, request
from psycopg2 import errorcodes

from database.queries import database_shows, database_user
from logic.user_handler import user_validation, hash_handler
from logic.data_handler import data_format, data_validation


app = Flask('codecool_series')
app.secret_key = "Don'tlooseurhead"


@app.route('/')
def index():
    try:
        genres = data_validation.validate_genres_list()
        return render_template('mainpage.html',
                               genres=genres)
    except data_validation.InvalidData:
        return ('mainpage_no_genres.html')


@app.route('/shows_by_genre', methods=['POST'])
def get_shows_by_genre():
    genre = request.form.get('genre')
    try:
        shows = data_validation.validate_shows_by_genres_list(genre)
        return render_template('shows_by_genre.html',
                               shows=shows,
                               genre=genre)
    except data_validation.InvalidData:
        return render_template('shows_by_genre.html',
                               genre=genre)


@app.route('/shows', methods=["GET"])
def show_mainpage():
    try:
        shows = data_validation.validate_shows()
        json_shows = json.dumps(shows)
        return json_shows
    except data_validation.InvalidData:
        return render_template('error_url.html')


@app.route('/<show_id>')
def display_show_details(show_id):
    try:
        data_validation.check_datatype_integer(show_id)
        show = data_validation.validate_show_details(show_id)
        actors= data_validation.validate_actors_by_showid(show['id'])
        return render_template('show_details.html',
                               show=show,
                               actors=actors)

    except data_validation.InvalidFormat:
        return render_template('error_url.html')
    except data_validation.InvalidData:
        return render_template('error_url.html')


@app.route('/seasons/<show_id>')
def display_show_seasons(show_id):
    try:
        data_validation.check_datatype_integer(show_id)    # if show_id != int => InvalidFormat
        data_format.get_show_by_id_from_database(show_id)  # if show_id not in db => InvalidData
        seasons = data_validation.validate_seasons_by_showId(show_id)
        title = data_validation.validate_show_title(show_id)
        seasons_episodes = data_validation.validate_episodes_by_show_and_seasons(seasons)
        return render_template('show_seasons.html',
                               seasons=seasons_episodes,
                               show=show_id,
                               title=title['title'])

    except data_validation.InvalidFormat:
        return render_template('error_url.html')
    except data_validation.InvalidData:
        return render_template('error_url.html')


@app.route('/seasons/<show_id>/episodes', methods=['GET'])
def display_episodes(show_id):
    try:
        data_validation.check_datatype_integer(show_id)    # if show_id != int => InvalidFormat
        data_format.get_show_by_id_from_database(show_id)  # if show_id not in db => InvalidData
        seasons = data_validation.validate_seasons_by_showId(show_id)
        seasons_episodes = data_validation.validate_episodes_by_show_and_seasons(seasons)
        return json.dumps(seasons_episodes)

    except data_validation.InvalidFormat:
        return render_template('error_url.html')
    except data_validation.InvalidData:
        return render_template('error_url.html')



@app.route('/actors')
def display_actors():
    try:
        actors = data_validation.validate_actors_list()
        return render_template('actors.html',
                               actors=actors)
    except data_validation.InvalidData:
        return render_template('error_url.html')

@app.route('/actors/min')
def display_actors_who_played_in_X_movies():
    try:
        X = request.args['min']
        actors = data_validation.validate_min_parameter(X)
        return render_template('actors_minXmovies.html',
                               actors = actors,
                               min=X)
    except data_validation.InvalidFormat:
        return render_template('error_url.html')
    except KeyError:
        return render_template('error_url.html')


@app.route('/actors/details', methods=['GET'])
def get_data_actors():
    try:
        actors = data_validation.validate_actors_list()
        return json.dumps(actors)
    except data_validation.InvalidData:
        return render_template('error_url.html')



@app.route('/actors/add', methods=['POST','GET'])
def add_new_actor():
    name = request.get_json()['name']
    birthday = request.get_json()['birthday']
    death = request.get_json()['death']
    biography = request.get_json()['biography']
    actor = {'name': name,
             'birthday': birthday,
             'death':death,
             'biography': biography}

    try:
        data_validation.validate_new_actor(actor)
        message = 'Actor added to database'
        return json.dumps({'message': message})

    except data_validation.DoubledData:
        message = 'Actor already in database'
        return json.dumps({'message': message})





@app.route('/design')
def design():
    return render_template('design.html')


@app.route("/register", methods=['POST', 'GET'])
def register_new_user():
    username = request.get_json()['username']
    password = request.get_json()['password']

    if user_validation.check_user_in_database(username):
        message = 'User already in database'
        status = 2
        json_message = json.dumps({'message': message,
                                   'status': status})
        return json_message

    else:
        hashed_password = hash_handler.hash_password(password)
        user = {
            'username': username,
            'password': hashed_password}
        database_user.register_new_user(user)
        session['username'] = user['username']

        message = "Registration successful"
        status = 1
        username = user['username']
        json_message = json.dumps({'message': message,
                                   'status': status,
                                   'username': username})
        return json_message


@app.route('/login', methods=['POST', 'GET'])
def login_user():
    log_user = {
        'username': request.get_json()['username'],
        'password': request.get_json()['password']
    }

    if user_validation.check_user_in_database(log_user['username']):
        let_pass = user_validation.verify_user(log_user)

        if let_pass:
            session['username'] = log_user['username']
            message = "Log in successful"
            status = 1
            username = log_user['username']
            json_message = json.dumps({'message': message,
                                       'status': status,
                                       'username': username})
            return json_message

        else:
            message = "Wrong password. Try again."
            status = 2
            json_message = json.dumps({'message': message,
                                       'status': status})
            return json_message
    else:
        message = "User doesn't exist. Please register"
        status = 3
        json_message = json.dumps({'message': message,
                                   'status': status})
        return json_message


@app.route('/logout')
def logout():
    del session['username']
    return redirect('/')


@app.route('/main')
def main():
    try:
        genres = data_validation.validate_genres_list()
        return render_template('main.html',
                               genres=genres)
    except data_validation.InvalidData:
        return ('main.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
