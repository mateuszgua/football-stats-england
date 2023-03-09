import mysql.connector as msql
from mysql.connector import Error

import config

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
        # cursor.execute(
        #     "CREATE TABLE teams(id INT PRIMARY KEY, name VARCHAR(255))")
        # print("Table teams created...")
        # cursor.execute(
        #     "CREATE TABLE games(id INT PRIMARY KEY, date DATE, HomeTeam INT, AwayTeam INT, FullTimeHomeGoals INT, FullTimeAwayGoals INT,"
        #     + "FullTimeResult VARCHAR(1), HalfTimeHomeGoals INT, HalfTimeAwayGoals INT, HalfTimeResult INT, HomeShots INT, AwayShots INT,"
        #     + "HomeShotsTarget INT, AwayShotsTarget INT, HomeFouls INT, AwayFouls INT, HomeCorners INT, AwayCorners INT, HomeYellowCards INT,"
        #     + "AwayYellowCards INT, HomeRedCards INT, AwayRedCards INT)")
        # print("Table teams created...")
        cursor.execute(
            "CREATE TABLE bets(id INT PRIMARY KEY, B365H NUMERIC, B365D NUMERIC, B365A NUMERIC, BWH NUMERIC, BWD NUMERIC, BWA NUMERIC,"
            + "GBH NUMERIC, GBD NUMERIC, GBA NUMERIC, IWH NUMERIC, IWD NUMERIC, IWA NUMERIC, LBH NUMERIC, LBD NUMERIC, LBA NUMERIC, SBH NUMERIC, SBD NUMERIC,"
            + "SBA NUMERIC, WHH NUMERIC, WHD NUMERIC, WHA NUMERIC, SJH NUMERIC, SJD NUMERIC, SJA NUMERIC, VCH NUMERIC, VCD NUMERIC, VCA NUMERIC,"
            + "Bb1X2 NUMERIC, BbMxH NUMERIC, BbAvH NUMERIC, BbMxD NUMERIC, BbAvD NUMERIC, BbMxA NUMERIC, BbAvA NUMERIC, BbOU NUMERIC, BbMxG2_5 NUMERIC, BbAvG2_5 NUMERIC, BbMxS2_5 NUMERIC,"
            + "BbAvS2_5 NUMERIC, BbAH NUMERIC, BbAHh NUMERIC, BbMxAHH NUMERIC, BbAvAHH NUMERIC, BbMxAHA NUMERIC, BbAvAHA NUMERIC)")
        print("Table teams created...")
except Error as e:
    print("Error while connecting to MySQL", e)
