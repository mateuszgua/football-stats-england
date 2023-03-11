import pandas as pd

import config

from my_database import MyDatabase


class DatabaseFillTables:

    def __init__(self) -> None:
        self.my_db = MyDatabase()

    def get_csv_files(self):

        try:
            self.games_data = pd.read_csv('games_table.csv')
            self.referee_data = pd.read_csv('referee_names.csv')
            self.bet_data = pd.read_csv('bet_table.csv')
            self.club_data = pd.read_csv('club_names.csv')
        except:
            print("Error, file or directory not exist!")

    def fill_referees(self):
        cursor = self.my_db.get_cursor()
        self.get_csv_files()
        sql = f"""INSERT INTO {config.Config.DB_NAME}.referee VALUES (%s, %s)"""
        self.referee_data = self.referee_data.drop(columns=['Id'])
        referee_list = self.referee_data.to_records().tolist()
        cursor.executemany(sql, referee_list)

    def fill_teams(self):
        cursor = self.my_db.get_cursor()
        self.get_csv_files()
        sql = f"""INSERT INTO {config.Config.DB_NAME}.teams VALUES (%s, %s)"""
        self.club_data = self.club_data.drop(columns=['Id'])
        club_list = self.club_data.to_records().tolist()
        cursor.executemany(sql, club_list)

    def fill_games(self):
        cursor = self.my_db.get_cursor()
        self.get_csv_files()
        sql = f"""INSERT INTO {config.Config.DB_NAME}.games VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        self.games_data = self.games_data.drop(columns=['Id'])
        games_list = self.games_data.to_records().tolist()
        cursor.executemany(sql, games_list)

    def fill_bets(self):
        cursor = self.my_db.get_cursor()
        self.get_csv_files()
        sql = f"""INSERT INTO {config.Config.DB_NAME}.bets VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        self.bet_data = self.bet_data.drop(columns=['Id'])
        bet_list = self.bet_data.to_records().tolist()
        cursor.executemany(sql, bet_list)
