import randomcolor
from matplotlib import pyplot as plt
from flask import Flask
from flask import render_template
from flask import send_file
from flask import request
from flask import redirect
from flask import url_for
from mysql.connector import Error
import pandas as pd
import matplotlib

from config import Config
from my_database import MyDatabase

matplotlib.use('Agg')

config = Config()
app = Flask(__name__, instance_relative_config=False)


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
        sql_file_task1 = "../sql_files/task_1.sql"
        df_task1 = get_dataframe_from_sql(sql_file_task1)
        df_task1.columns = ['Club', 'Wins']
        sql_file_task2 = "../sql_files/task_2.sql"
        df_task2 = get_dataframe_from_sql(sql_file_task2)
        df_task2.columns = ['Club', 'TotalPoints']
        sql_file_task3 = "../sql_files/task_3.sql"
        df_task3 = get_dataframe_from_sql(sql_file_task3)
        df_task3.columns = ['Club', 'TotalGames']
        sql_file_task4 = "../sql_files/task_4.sql"
        df_task4 = get_dataframe_from_sql(sql_file_task4)
        df_task4.columns = ['Season', 'AvgGoals']
        sql_file_task5 = "../sql_files/task_5.sql"
        df_task5 = get_dataframe_from_sql(sql_file_task5)
        df_task5.columns = ['Season', 'NumberDraws']
        sql_file_task6 = "../sql_files/task_6.sql"
        df_task6 = get_dataframe_from_sql(sql_file_task6)
        df_task6.columns = ['Season', 'SumFirstHalfGoals',
                            'SumSecoundHalfGoals', 'AvgFirstHalfGoals', 'AvgSecoundHalfGoals']
        sql_file_task7 = "../sql_files/task_7.sql"
        df_task7 = get_dataframe_from_sql(sql_file_task7)
        df_task7.columns = ['Season', 'AvgShots',
                            'AvgCorners', 'AvgFouls', 'AvgYellowCards', 'AvgRedCards']
        sql_file_task8 = "../sql_files/task_8.sql"
        df_task8 = get_dataframe_from_sql(sql_file_task8)
        df_task8.columns = ['Season', 'Club',
                            'Points', 'Goals', 'Fouls', 'Corners', 'YellowCards', 'RedCards']
        sql_file_task9 = "../sql_files/task_9.sql"
        df_task9 = get_dataframe_from_sql(sql_file_task9)
        df_task9.columns = ['Name', 'NumberMatches']
        sql_file_task10 = "../sql_files/task_10.sql"
        df_task10 = get_dataframe_from_sql(sql_file_task10)
        df_task10.columns = ['Name', 'YellowCards']
        sql_file_task11 = "../sql_files/task_11.sql"
        df_task11 = get_dataframe_from_sql(sql_file_task11)
        df_task11.columns = ['Season', 'Name', 'RedCards']
        sql_file_task12 = "../sql_files/task_12.sql"
        df_task12 = get_dataframe_from_sql(sql_file_task12)
        df_task12.columns = ['NumberMatches', 'IsCorrectType']
    except Error as e:
        print(e)
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
                               column_names8=df_task8.columns.values,
                               row_data8=list(df_task8.values.tolist()),
                               zip8=zip,
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


@app.route('/visualization')
def visualization():
    try:
        font1 = {'family': 'serif', 'color': 'black', 'size': 25}
        font2 = {'family': 'serif', 'color': 'black', 'size': 15}

        list_numbers = list(range(1, 21))
        sql_file_task_vis_1_3 = "../sql_files/task_vis_1_3.sql"
        df_task_vis_1_3 = get_dataframe_from_sql(sql_file_task_vis_1_3)

        list_seasons_short = []
        for i in df_task_vis_1_3[0]:
            list_seasons_short.append(i)
        list_seasons = [s.replace('Ses', 'Season ')
                        for s in list_seasons_short]
        dict_seasons = {list_seasons_short[i]: list_seasons[i]
                        for i in range(len(list_seasons_short))}
        sql_file_task_vis_1 = "../sql_files/task_vis_1.sql"
        create_sql_procedure(sql_file_task_vis_1)

        sql_file_task_vis_2 = "../sql_files/task_vis_2.sql"
        df_task_vis_2 = get_dataframe_from_sql(sql_file_task_vis_2)
        df_task_vis_2.columns = ['Season', 'Club', 'Points']

        number_of_colors = len(df_task_vis_2['Club']) - 1

        colors = []
        for i in range(number_of_colors):
            i = randomcolor.RandomColor().generate()
            colors.append(i)
        color_list = [item for sublist in colors for item in sublist]

        plt.figure(figsize=(20, 10))
        plt.bar(df_task_vis_2["Season"],
                df_task_vis_2["Points"],
                label=df_task_vis_2["Club"], color=color_list, width=0.5)
        plt.title("The winning team with number of points per season",
                  fontdict=font1)
        plt.xlabel('Season', fontdict=font2)
        plt.xticks(rotation=70)
        plt.ylabel('Points', fontdict=font2)
        plt.legend(bbox_to_anchor=(1, 1), loc="upper left",
                   frameon=False, fontsize=12)
        plt.savefig('../static/charts/chart_task_2.png')
        plt.close()

        sql_file_task_vis_3 = "../sql_files/task_vis_3.sql"
        df_task_vis_3 = get_dataframe_from_sql(sql_file_task_vis_3)
        df_task_vis_3.columns = ['Season', 'Goals']

        plt.figure(figsize=(20, 10))
        plt.plot(df_task_vis_3["Season"],
                 df_task_vis_3["Goals"],
                 c='#0dbcae', marker='o')
        plt.title("Total golas per season", fontdict=font1)
        plt.xlabel('Season', fontdict=font2)
        plt.xticks(rotation=70)
        plt.ylabel('Goals', fontdict=font2)
        plt.grid()

        for x, y in zip(df_task_vis_3["Season"], df_task_vis_3["Goals"]):
            label = "{:.0f}".format(y)

            plt.annotate(label,
                         (x, y),
                         textcoords="offset points",
                         xytext=(0, 15),
                         ha='center',
                         arrowprops=dict(arrowstyle="->", color='black'),
                         fontsize=12)

        plt.savefig('../static/charts/chart_task_3.png')
        plt.close()
    except Error as e:
        print(e)
    finally:
        return render_template('visualization.html', seasons=dict_seasons, positions=list_numbers)


@app.route("/chart", methods=['GET', 'POST'])
def chart():
    try:
        season = request.form.get('season')
        place = request.form.get('place')

        my_db = MyDatabase()
        cursor = my_db.get_cursor()

        args = (int(place), season, (0, 'CHAR'), (0, 'CHAR'), (0))
        result_args = cursor.callproc('GetTeamResultFromSeason', args)
        result = [result_args[2], result_args[3], result_args[4]]
        result_df = pd.DataFrame(result)
        result_df_transposed = result_df.transpose()
        result_df_transposed.columns = ['Season', 'Club', 'Points']
        label = result_df_transposed["Club"][0]

        font1 = {'family': 'serif', 'color': 'black', 'size': 25}
        font2 = {'family': 'serif', 'color': 'black', 'size': 15}
        plt.figure(figsize=(20, 10))
        plt.scatter(result_df_transposed["Season"],
                    result_df_transposed["Points"],
                    label=label,
                    color='green')
        plt.title("The team with number of points for selected eason",
                  fontdict=font1)
        plt.xlabel('Season', fontdict=font2)
        plt.xticks(rotation=0, fontsize=15)
        plt.ylabel('Points', fontdict=font2)
        for x, y in zip(result_df_transposed["Season"], result_df_transposed["Points"]):
            label = "{:.0f}".format(y)

            plt.annotate(label,
                         (x, y),
                         textcoords="offset points",
                         xytext=(0, 20),
                         ha='center',
                         arrowprops=dict(arrowstyle="->", color='black'),
                         fontsize=15)

        plt.legend(loc='lower center', frameon=False, fontsize=15)
        plt.savefig('../static/charts/chart_task_1.png')
        plt.close()
    except Error as e:
        print(e)
    finally:
        return redirect(url_for('visualization'))


def get_dataframe_from_sql(sql_file_path):
    try:
        my_db = MyDatabase()
        cursor = my_db.get_cursor()
        sql_file = open(sql_file_path)
        sql_as_string = sql_file.read()
        cursor.execute(sql_as_string)
        result = cursor.fetchall()
        result_df = pd.DataFrame(result)
    except Error as e:
        print(e)
    finally:
        sql_file.close()
        return result_df


def create_sql_procedure(sql_file_path):
    try:
        my_db = MyDatabase()
        cursor = my_db.get_cursor()
        sql_file = open(sql_file_path)
        sql_as_string = sql_file.read()
        cursor.execute(sql_as_string)
    except Error as e:
        print(e)
    finally:
        sql_file.close()


@ app.route('/documentation')
def documentation():
    return render_template('documentation.html')
