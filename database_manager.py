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

        # sql = """INSERT INTO referee VALUES (%s, %s)"""
        # referee_data = referee_data.drop(columns=['Id'])
        # referee_list = referee_data.to_records().tolist()
        # cursor = conn.cursor()
        # cursor.executemany(sql, referee_list)
        # conn.commit()

        # sql = """INSERT INTO teams VALUES (%s, %s)"""
        # club_data = club_data.drop(columns=['Id'])
        # club_list = club_data.to_records().tolist()
        # cursor = conn.cursor()
        # cursor.executemany(sql, club_list)
        # conn.commit()

        # sql = """INSERT INTO games VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        # games_data = games_data.drop(columns=['Id'])
        # games_list = games_data.to_records().tolist()
        # cursor = conn.cursor()
        # cursor.executemany(sql, games_list)
        # conn.commit()

        # sql = """INSERT INTO football_eng.bets VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        # bet_data = bet_data.drop(columns=['Id'])
        # bet_list = bet_data.to_records().tolist()
        # cursor = conn.cursor()
        # cursor.executemany(sql, bet_list)
        # conn.commit()
