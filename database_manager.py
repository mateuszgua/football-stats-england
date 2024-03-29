from config import Config
from my_database import MyDatabase
from database_fill_tables import DatabaseFillTables
from database_reader import DatabaseReader


class DatabaseManager:

    def __init__(self) -> None:
        self.db = MyDatabase()

    def create_database(self):
        sql_create = f"""CREATE DATABASE IF NOT EXISTS {Config.DB_NAME}"""
        self.db.sql_execute(sql_create)

    def create_tables(self):
        try:
            read_from_db = DatabaseReader()
            fill_table = DatabaseFillTables()
            sql_create = (
                f"""CREATE TABLE IF NOT EXISTS {Config.DB_NAME}.referee(id INT PRIMARY KEY, name VARCHAR(255))""")
            self.db.sql_execute(sql_create)

            if read_from_db.is_table_not_empty('referee') is False:
                fill_table.fill_referees()

            sql_create = (
                f"""CREATE TABLE IF NOT EXISTS {Config.DB_NAME}.clubs(id INT PRIMARY KEY, name VARCHAR(255))""")
            self.db.sql_execute(sql_create)
            if read_from_db.is_table_not_empty('clubs') is False:
                fill_table.fill_clubs()

            sql_create = (f"""CREATE TABLE IF NOT EXISTS {Config.DB_NAME}.games(id INT PRIMARY KEY, date DATE, HomeTeam INT, AwayTeam INT, FullTimeHomeGoals INT, FullTimeAwayGoals INT,"""
                          + """FullTimeResult VARCHAR(10), HalfTimeHomeGoals INT, HalfTimeAwayGoals INT, HalfTimeResult VARCHAR(10), Referee INT, HomeShots INT, AwayShots INT,"""
                          + """HomeShotsTarget INT, AwayShotsTarget INT, HomeFouls INT, AwayFouls INT, HomeCorners INT, AwayCorners INT, HomeYellowCards INT,"""
                          + """AwayYellowCards INT, HomeRedCards INT, AwayRedCards INT, Season VARCHAR(15))""")
            self.db.sql_execute(sql_create)
            if read_from_db.is_table_not_empty('games') is False:
                fill_table.fill_games()

            sql_create = (
                f"""CREATE TABLE IF NOT EXISTS {Config.DB_NAME}.bets(id INT PRIMARY KEY, B365H FLOAT, B365D FLOAT, B365A FLOAT, BWH FLOAT, BWD FLOAT, BWA FLOAT,"""
                + """GBH FLOAT, GBD FLOAT, GBA FLOAT, IWH FLOAT, IWD FLOAT, IWA FLOAT, LBH FLOAT, LBD FLOAT, LBA FLOAT, SBH FLOAT, SBD FLOAT,"""
                + """SBA FLOAT, WHH FLOAT, WHD FLOAT, WHA FLOAT, SJH FLOAT, SJD FLOAT, SJA FLOAT, VCH FLOAT, VCD FLOAT, VCA FLOAT,"""
                + """Bb1X2 FLOAT, BbMxH FLOAT, BbAvH FLOAT, BbMxD FLOAT, BbAvD FLOAT, BbMxA FLOAT, BbAvA FLOAT, BbOU FLOAT, BbMxG2_5 FLOAT, BbAvG2_5 FLOAT, BbMxS2_5 FLOAT,"""
                + """BbAvS2_5 FLOAT, BbAH FLOAT, BbAHh FLOAT, BbMxAHH FLOAT, BbAvAHH FLOAT, BbMxAHA FLOAT, BbAvAHA FLOAT)""")
            self.db.sql_execute(sql_create)
            if read_from_db.is_table_not_empty('bets') is False:
                fill_table.fill_bets()

        finally:
            print("Tables created successfully.")
