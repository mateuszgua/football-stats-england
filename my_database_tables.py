import mysql.connector as msql
from mysql.connector import Error
import pandas as pd

import config

try:
    games_data = pd.read_csv('games_table.csv')
    referee_data = pd.read_csv('referee_names.csv')
    bet_data = pd.read_csv('bet_table.csv')
    club_data = pd.read_csv('club_names.csv')
except:
    print("Error, file or directory not exist!")
configuration = config.Config()

try:
    conn = msql.connect(host=configuration.HOST,
                        database=configuration.DB_NAME,
                        user=configuration.USERNAME,
                        password=configuration.PASSWORD)
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        # cursor.execute("DROP TABLE IF EXIST referee;")
        print("Creating table...")

        # cursor.execute(
        #     "CREATE TABLE referee(id INT PRIMARY KEY, name VARCHAR(255))")
        # print("Table referee created...")

        # sql = """INSERT INTO referee VALUES (%s, %s)"""
        # referee_data = referee_data.drop(columns=['Id'])
        # referee_list = referee_data.to_records().tolist()
        # cursor = conn.cursor()
        # cursor.executemany(sql, referee_list)
        # conn.commit()

        # cursor.execute(
        #     "CREATE TABLE teams(id INT PRIMARY KEY, name VARCHAR(255))")
        # print("Table teams created...")

        # sql = """INSERT INTO teams VALUES (%s, %s)"""
        # club_data = club_data.drop(columns=['Id'])
        # club_list = club_data.to_records().tolist()
        # cursor = conn.cursor()
        # cursor.executemany(sql, club_list)
        # conn.commit()

        # cursor.execute(
        #     "CREATE TABLE games(id INT PRIMARY KEY, date DATE, HomeTeam INT, AwayTeam INT, FullTimeHomeGoals INT, FullTimeAwayGoals INT,"
        #     + "FullTimeResult VARCHAR(10), HalfTimeHomeGoals INT, HalfTimeAwayGoals INT, HalfTimeResult VARCHAR(10), HomeShots INT, AwayShots INT,"
        #     + "HomeShotsTarget INT, AwayShotsTarget INT, HomeFouls INT, AwayFouls INT, HomeCorners INT, AwayCorners INT, HomeYellowCards INT,"
        #     + "AwayYellowCards INT, HomeRedCards INT, AwayRedCards INT)")
        # print("Table teams created...")

        # sql = """INSERT INTO games VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        # games_data = games_data.drop(columns=['Id'])
        # games_list = games_data.to_records().tolist()
        # cursor = conn.cursor()
        # cursor.executemany(sql, games_list)
        # conn.commit()

        cursor.execute(
            "CREATE TABLE bets(id INT PRIMARY KEY, B365H FLOAT, B365D FLOAT, B365A FLOAT, BWH FLOAT, BWD FLOAT, BWA FLOAT,"
            + "GBH FLOAT, GBD FLOAT, GBA FLOAT, IWH FLOAT, IWD FLOAT, IWA FLOAT, LBH FLOAT, LBD FLOAT, LBA FLOAT, SBH FLOAT, SBD FLOAT,"
            + "SBA FLOAT, WHH FLOAT, WHD FLOAT, WHA FLOAT, SJH FLOAT, SJD FLOAT, SJA FLOAT, VCH FLOAT, VCD FLOAT, VCA FLOAT,"
            + "Bb1X2 FLOAT, BbMxH FLOAT, BbAvH FLOAT, BbMxD FLOAT, BbAvD FLOAT, BbMxA FLOAT, BbAvA FLOAT, BbOU FLOAT, BbMxG2_5 FLOAT, BbAvG2_5 FLOAT, BbMxS2_5 FLOAT,"
            + "BbAvS2_5 FLOAT, BbAH FLOAT, BbAHh FLOAT, BbMxAHH FLOAT, BbAvAHH FLOAT, BbMxAHA FLOAT, BbAvAHA FLOAT)")
        print("Table teams created...")

        sql = """INSERT INTO football_eng.bets VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        bet_data = bet_data.drop(columns=['Id'])
        bet_list = bet_data.to_records().tolist()
        cursor = conn.cursor()
        cursor.executemany(sql, bet_list)
        conn.commit()

        # sql = "SELECT * FROM referee"
        # cursor.execute(sql)
        # result = cursor.fetchall()
        # for i in result:
        #     print(i)

except Error as e:
    print("Error while connecting to MySQL", e)
