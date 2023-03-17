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
    try:
        sql_file_task1 = "./sql_files/task_1.sql"
        df_task1 = get_dataframe_from_sql(sql_file_task1)
        df_task1.columns = ['Club', 'Wins']
        sql_file_task2 = "./sql_files/task_2.sql"
        df_task2 = get_dataframe_from_sql(sql_file_task2)
        df_task2.columns = ['Club', 'TotalPoints']
        sql_file_task3 = "./sql_files/task_3.sql"
        df_task3 = get_dataframe_from_sql(sql_file_task3)
        df_task3.columns = ['Club', 'TotalGames']
        sql_file_task4 = "./sql_files/task_4.sql"
        df_task4 = get_dataframe_from_sql(sql_file_task4)
        df_task4.columns = ['Season', 'AvgGoals']
        sql_file_task5 = "./sql_files/task_5.sql"
        df_task5 = get_dataframe_from_sql(sql_file_task5)
        df_task5.columns = ['Season', 'NumberDraws']
        sql_file_task6 = "./sql_files/task_6.sql"
        df_task6 = get_dataframe_from_sql(sql_file_task6)
        df_task6.columns = ['Season', 'SumFirstHalfGoals',
                            'SumSecoundHalfGoals', 'AvgFirstHalfGoals', 'AvgSecoundHalfGoals']
        sql_file_task7 = "./sql_files/task_7.sql"
        df_task7 = get_dataframe_from_sql(sql_file_task7)
        df_task7.columns = ['Season', 'AvgShots',
                            'AvgCorners', 'AvgFouls', 'AvgYellowCards', 'AvgRedCards']
        sql_file_task9 = "./sql_files/task_9.sql"
        df_task9 = get_dataframe_from_sql(sql_file_task9)
        df_task9.columns = ['Name', 'NumberMatches']
        sql_file_task10 = "./sql_files/task_10.sql"
        df_task10 = get_dataframe_from_sql(sql_file_task10)
        df_task10.columns = ['Name', 'YellowCards']
        sql_file_task11 = "./sql_files/task_11.sql"
        df_task11 = get_dataframe_from_sql(sql_file_task11)
        df_task11.columns = ['Season', 'Name', 'RedCards']
        sql_file_task12 = "./sql_files/task_12.sql"
        df_task12 = get_dataframe_from_sql(sql_file_task12)
        df_task12.columns = ['NumberMatches', 'IsCorrectType']
    finally:
        return render_template('flask.html',
                               column_names1=df_task1.columns.values,
                               row_data1=list(df_task1.values.tolist()),
                               zip1=zip,
                               column_names2=df_task2.columns.values,
                               row_data2=list(df_task2.values.tolist()),
                               zip2=zip,
                               column_names3=df_task3.columns.values,
                               row_data3=list(df_task3.values.tolist()),
                               zip3=zip,
                               column_names4=df_task4.columns.values,
                               row_data4=list(df_task4.values.tolist()),
                               zip4=zip,
                               column_names5=df_task5.columns.values,
                               row_data5=list(df_task5.values.tolist()),
                               zip5=zip,
                               column_names6=df_task6.columns.values,
                               row_data6=list(df_task6.values.tolist()),
                               zip6=zip,
                               column_names7=df_task7.columns.values,
                               row_data7=list(df_task7.values.tolist()),
                               zip7=zip,
                               column_names9=df_task9.columns.values,
                               row_data9=list(df_task9.values.tolist()),
                               zip9=zip,
                               column_names10=df_task10.columns.values,
                               row_data10=list(df_task10.values.tolist()),
                               zip10=zip,
                               column_names11=df_task11.columns.values,
                               row_data11=list(df_task11.values.tolist()),
                               zip11=zip,
                               column_names12=df_task12.columns.values,
                               row_data12=list(df_task12.values.tolist()),
                               zip12=zip,
                               )


def get_dataframe_from_sql(sql_file_path):
    try:
        my_db = MyDatabase()
        cursor = my_db.get_cursor()
        sql_file = open(sql_file_path)
        sql_as_string = sql_file.read()
        cursor.execute(sql_as_string)
        result = cursor.fetchall()
        result_df = pd.DataFrame(result)
    finally:
        sql_file.close()
        return result_df


@app.route('/visualization')
def visualization():
    return render_template('visualization.html')


@app.route('/schema')
def schema():
    return render_template('schema.html')


if __name__ == '__main__':
    app.run()
