import glob
import pandas as pd

from helpers import Helpers
from append_csv_files import AppendCsvFiles


class CreateCsvNormalizeTables:

    def __init__(self) -> None:

        self.all_data = self.get_full_data_file()

    def get_full_data_file(self):
        helper = Helpers()
        append_files = AppendCsvFiles()
        path_full_data = '../data/append_files.csv'
        if helper.is_file_exist(path_full_data) is False:
            append_files.create_full_data_table(path_full_data)
        self.all_data = pd.read_csv(path_full_data)
        return self.all_data

    def create_club_names_table(self, path):
        unique_values = self.all_data['HomeTeam'].unique()
        cleared_nan = [x for x in unique_values if str(x) != 'nan']
        club_names = pd.DataFrame(cleared_nan, columns=['Name'])

        file_exist = glob.glob(path)

        if not file_exist:
            club_names.to_csv(path, index=True,
                              index_label='Id', encoding='utf-8-sig')
            return 'File save successfully!'
        else:
            return 'File already exists!'

    def create_referee_names_table(self, path):
        unique_values = self.all_data['Referee'].unique()
        cleared_nan = [x for x in unique_values if str(x) != 'nan']

        splited_names = []
        for i in cleared_nan:
            splited = i.split()
            splited_names.append(splited)

        lastnames = []
        for lastname in splited_names:
            x = lastname[0].find(',')
            if x != -1:
                lastnames.append(lastname[0].replace(',', ''))
            elif (len(lastname[0]) <= 2) and (len(lastname[1]) != 1 and len(lastname[1]) != 2):
                lastnames.append(lastname[1])
            elif (len(lastname[0]) <= 2) and (len(lastname[1]) <= 2):
                lastnames.append(lastname[2])
            elif (len(lastname[0]) > 1) and (len(lastname[1]) <= 2):
                lastnames.append(lastname[0])
            elif len(lastname[0]) > 1 and len(lastname[1]) > 1:
                lastnames.append(lastname[1])

        lastnames = [*set(lastnames)]
        df_referee_names = pd.DataFrame(lastnames, columns=['Name'])

        file_exist = glob.glob(path)

        if not file_exist:
            df_referee_names.to_csv(path, index=True,
                                    index_label='Id', encoding='utf-8-sig')
            return 'File save successfully!'
        else:
            return 'File already exists!'

    def create_bets_table(self, path):
        bet_table = self.all_data[self.all_data.columns[23:68]]
        cleared_nan = bet_table.fillna('9999')

        file_exist = glob.glob(path)

        if not file_exist:
            cleared_nan.to_csv(path, index=True,
                               index_label='Id', encoding='utf-8-sig')
            return 'File save successfully!'
        else:
            return 'File already exists!'

    def create_games_table(self, path, path_club):
        games_table = self.all_data[self.all_data.columns[1:23]]
        games_drop_referee = games_table.drop(['Referee'], axis=1)
        cleared_nan = games_drop_referee.fillna('9999')

        club_names = pd.read_csv(path_club)

        cleared_nan['HomeTeam'] = cleared_nan['HomeTeam'].map(
            club_names.set_index('Name')['Id'])
        cleared_nan['AwayTeam'] = cleared_nan['AwayTeam'].map(
            club_names.set_index('Name')['Id'])
        cleared_nan['Date'] = cleared_nan['Date'].replace(['Null'], '01/01/51')
        cleared_nan['Date'] = pd.to_datetime(
            cleared_nan['Date'], errors='coerce', format='%d/%m/%y').dt.strftime('%Y-%m-%d')
        cleared_nan = cleared_nan.fillna(
            {'Date': '1900-01-01', 'HomeTeam': 9999, 'AwayTeam': 9999})

        file_exist = glob.glob(path)

        if not file_exist:
            cleared_nan.to_csv(path, index=True,
                               index_label='Id', encoding='utf-8-sig')
            return 'File save successfully!'
        else:
            return 'File already exists!'


# response = CreateCsvNormalizeTables()
# response.create_club_names_table()
# response = CreateCsvNormalizeTables()
# response.create_referee_names_table()
# response = CreateCsvNormalizeTables()
# response.create_bets_table()
# response = CreateCsvNormalizeTables()
# response.create_games_table()
