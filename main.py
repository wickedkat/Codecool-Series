from flask import Flask, render_template, json, session, redirect, request

from database.queries import database_shows
from logic.data_handler import data_validation


app = Flask('codecool_series')
app.secret_key="Don'tlooseurhead"



@app.route('/')
def index():
    try:
        genres = data_validation.validate_genres_list()
        return render_template('mainpage.html',
                               genres=genres)
    except data_validation.InvalidData:
        return render_template('mainpage_no_genres.html')


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
def display_show_seasons(show_id):
    try:
        data_validation.check_datatype_integer(show_id)
        seasons = data_validation.validate_seasons(show_id)
        show = data_validation.validate_show_by_id(show_id)
        return render_template('show_seasons.html',
                               seasons = seasons,
                               show = show)
    except data_validation.InvalidFormat:
        return render_template('error_url.html')
    except data_validation.InvalidData:
        return render_template('error_url.html')


@app.route('/<season_id>/episodes')
def display_episodes_by_season(season_id):
    try:
        data_validation.check_datatype_integer(season_id)
        episodes = data_validation.validate_episodes(season_id)
        show = data_validation.validate_show_by_seasonId(season_id)
        return render_template('episodes.html',
                               episodes = episodes,
                               show = show)
    except data_validation.InvalidFormat:
        return render_template('error_url.html')
    except data_validation.InvalidData:
        return render_template('error_url.html')


@app.route('/<season_id>/episodes/<episode_id>')
def display_episode_details(season_id, episode_id):
    try:
        data_validation.check_datatype_integer(season_id)
        data_validation.check_datatype_integer(episode_id)
        return render_template('blank.html')

    except data_validation.InvalidFormat:
        return render_template('error_url.html')


@app.route('/actors')
def display_actors():
    try:
        actors = data_validation.validate_actors_list()
        return render_template('actors.html',
                               actors=actors)
    except data_validation.InvalidData:
        return render_template('error_url.html')

@app.route('/actors/<actor_id>')
def get_actor_roles(actor_id):
    try:
        data_validation.check_datatype_integer(actor_id)
        actor = data_validation.validate_actor(actor_id)
        return json.dumps(actor)

    except data_validation.InvalidFormat:
        return render_template('error_url.html')
    except data_validation.InvalidData:
        return render_template('error_url.html')





@app.route('/design')
def design():
    return render_template('design.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        port=8000
    )



