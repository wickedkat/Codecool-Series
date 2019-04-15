from flask import Flask, render_template, json, session, redirect, request

from database.queries import database_shows


app = Flask('codecool_series')
app.secret_key="Don'tlooseurhead"



@app.route('/')
def index():
    shows =  database_shows.get_just_shows()
    return render_template('index.html',
                           shows = shows)


@app.route('/design')
def design():
    return render_template('design.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        port=8000
    )



