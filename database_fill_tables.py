import os
import pandas as pd

import config

from my_database import MyDatabase
from create_csv_normalize_tables import CreateCsvNormalizeTables
from helpers import Helpers


class DatabaseFillTables:

    def __init__(self) -> None:
        self.my_db = MyDatabase()

    def get_csv_files(self):
        create_table = CreateCsvNormalizeTables()
        helper = Helpers()

        try:
            path_clubs = '../data/club_names.csv'
            if helper.is_file_exist(path_clubs) is False:
                create_table.create_club_names_table(path_clubs)
            self.club_data = pd.read_csv(path_clubs)

            path_games = '../data/games_table.csv'
            path_clubs = '../data/club_names.csv'
            path_referees = '../data/referee_names.csv'
            if helper.is_file_exist(path_games) is False:
                create_table.create_games_table(
                    path_games, path_referees, path_clubs)
            self.games_data = pd.read_csv(path_games)

            path_referees = '../data/referee_names.csv'
            if helper.is_file_exist(path_referees) is False:
                create_table.create_referee_names_table(path_referees)
            self.referee_data = pd.read_csv(path_referees)

            path_bets = '../data/bet_table.csv'
            if helper.is_file_exist(path_bets) is False:
                create_table.create_bets_table(path_bets)
            self.bet_data = pd.read_csv(path_bets)

        except:
            print("Error, file or directory not exist!")

    def fill_referees(self):
        cursor = self.my_db.get_cursor()
        self.get_csv_files()
        sql = f"""INSERT INTO {config.Config.DB_NAME}.referee VALUES (%s, %s)"""
        self.referee_data = self.referee_data.drop(columns=['Id'])
        referee_list = self.referee_data.to_records().tolist()
        cursor.executemany(sql, referee_list)

    def fill_clubs(self):
        cursor = self.my_db.get_cursor()
        self.get_csv_files()
        sql = f"""INSERT INTO {config.Config.DB_NAME}.clubs VALUES (%s, %s)"""
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
