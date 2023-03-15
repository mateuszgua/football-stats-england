from flask import Flask
from flask import render_template
from flask import send_file
from flask import redirect
import pandas as pd

from my_database import MyDatabase

app = Flask(__name__, instance_relative_config=False)
app.config.from_object('flask_settings.Config')


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/source')
def source():
    return render_template('source.html')


@app.route('/download')
def download_file():
    path = './samples/sample_season_2020_2021.csv'
    return send_file(path, as_attachment=True)


@app.route('/normalization')
def normalization():
    return render_template('normalization.html')


@app.route('/database')
def database():
    return render_template('database.html')


@app.route('/flask')
def flask():
    my_db = MyDatabase()
    try:
        cursor = my_db.get_cursor()
        sql_file = open("./sql_files/task_1.sql")
        sql_as_string = sql_file.read()
        cursor.execute(sql_as_string)
        result = cursor.fetchall()
        df = pd.DataFrame(result)
        df.columns = ['Club', 'Wins']
    finally:
        sql_file.close()

    try:
        cursor = my_db.get_cursor()
        sql_file = open("./sql_files/task_2.sql")
        sql_as_string = sql_file.read()
        cursor.execute(sql_as_string)
        result = cursor.fetchall()
        df = pd.DataFrame(result)
        df.columns = ['Club', 'TotalPoints']
    finally:
        sql_file.close()

    try:
        cursor = my_db.get_cursor()
        sql_file = open("./sql_files/task_3.sql")
        sql_as_string = sql_file.read()
        cursor.execute(sql_as_string)
        result = cursor.fetchall()
        df = pd.DataFrame(result)
        df.columns = ['Club', 'TotalGames']
    finally:
        sql_file.close()

    # try:
    #     cursor = my_db.get_cursor()
    #     sql_file = open("./sql_files/task_4.sql")
    #     sql_as_string = sql_file.read()
    #     cursor.execute(sql_as_string)
    #     result = cursor.fetchall()
    #     df = pd.DataFrame(result)
    #     df.columns = ['Club', 'TotalGames']
    #     print(' ')
    #     print(df)
    #     print(' ')
    # finally:
    #     sql_file.close()
    return render_template('flask.html')


@app.route('/visualization')
def visualization():
    return render_template('visualization.html')


@app.route('/schema')
def schema():
    return render_template('schema.html')


if __name__ == '__main__':
    app.run()
