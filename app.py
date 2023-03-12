from flask import Flask
from flask import render_template
from flask import redirect

from database_reader import DatabaseReader

app = Flask(__name__, instance_relative_config=False)
app.config.from_object('flask_settings.Config')


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/source')
def source():
    return render_template('source.html')


@app.route('/normalization')
def normalization():
    return render_template('normalization.html')


@app.route('/database')
def database():
    return render_template('database.html')


@app.route('/flask')
def flask():
    return render_template('flask.html')


if __name__ == '__main__':
    app.run()
