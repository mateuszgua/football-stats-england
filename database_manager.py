from my_database import MyDatabase
import config


class DatabaseManager:

    def __init__(self) -> None:
        self.db = MyDatabase()

    def create_database(self):
        cursor = self.db.get_cursor()
        sql_create = f"""CREATE DATABASE IF NOT EXISTS football_eng"""
        cursor.execute(sql_create)

    def create_tables(self):
        cursor = self.db.get_cursor()

        try:
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS football_eng.referee(id INT PRIMARY KEY, name VARCHAR(255))""")
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS football_eng.teams(id INT PRIMARY KEY, name VARCHAR(255))""")
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS football_eng.games(id INT PRIMARY KEY, date DATE, HomeTeam INT, AwayTeam INT, FullTimeHomeGoals INT, FullTimeAwayGoals INT,"
                + "FullTimeResult VARCHAR(10), HalfTimeHomeGoals INT, HalfTimeAwayGoals INT, HalfTimeResult VARCHAR(10), HomeShots INT, AwayShots INT,"
                + "HomeShotsTarget INT, AwayShotsTarget INT, HomeFouls INT, AwayFouls INT, HomeCorners INT, AwayCorners INT, HomeYellowCards INT,"
                + "AwayYellowCards INT, HomeRedCards INT, AwayRedCards INT)")
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS football_eng.bets(id INT PRIMARY KEY, B365H FLOAT, B365D FLOAT, B365A FLOAT, BWH FLOAT, BWD FLOAT, BWA FLOAT,"
                + "GBH FLOAT, GBD FLOAT, GBA FLOAT, IWH FLOAT, IWD FLOAT, IWA FLOAT, LBH FLOAT, LBD FLOAT, LBA FLOAT, SBH FLOAT, SBD FLOAT,"
                + "SBA FLOAT, WHH FLOAT, WHD FLOAT, WHA FLOAT, SJH FLOAT, SJD FLOAT, SJA FLOAT, VCH FLOAT, VCD FLOAT, VCA FLOAT,"
                + "Bb1X2 FLOAT, BbMxH FLOAT, BbAvH FLOAT, BbMxD FLOAT, BbAvD FLOAT, BbMxA FLOAT, BbAvA FLOAT, BbOU FLOAT, BbMxG2_5 FLOAT, BbAvG2_5 FLOAT, BbMxS2_5 FLOAT,"
                + "BbAvS2_5 FLOAT, BbAH FLOAT, BbAHh FLOAT, BbMxAHH FLOAT, BbAvAHH FLOAT, BbMxAHA FLOAT, BbAvAHA FLOAT)")
        finally:
            print("Tables created successfully.")
