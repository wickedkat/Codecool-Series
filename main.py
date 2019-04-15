from flask import Flask, render_template, json, session, redirect, request

from database.queries import database_shows
from logic.data_handler import data_validation


app = Flask('codecool_series')
app.secret_key="Don'tlooseurhead"



@app.route('/')
def index():
    try:
        shows = database_shows.get_just_shows()
        genres = data_validation.validate_genres_list()
        return render_template('mainpage.html',
                               genres=genres,
                               shows = shows)
    except data_validation.InvalidData:
        return render_template('mainpage_no_genres.html')


@app.route('/design')
def design():
    return render_template('design.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        port=8000
    )



