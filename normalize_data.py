import os
import glob
import pandas as pd
import numpy as np

os.chdir("./data")

all_data = pd.read_csv('append_files.csv')
print(all_data)


def get_club_names():
    unique_values = all_data['HomeTeam'].unique()
    cleared_nan = [x for x in unique_values if str(x) != 'nan']
    club_names = pd.DataFrame(cleared_nan, columns=['Name'])

    filename = "club_names.csv"
    files_present = glob.glob(filename)

    if not files_present:
        club_names.to_csv(filename, index=True,
                          index_label='Id', encoding='utf-8-sig')
        return 'File save successfully!'
    else:
        return 'File already exists!'


response = get_club_names()
print(response)


def get_referee_names():
    unique_values = all_data['Referee'].unique()
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

    filename = "referee_names.csv"
    files_present = glob.glob(filename)

    if not files_present:
        df_referee_names.to_csv(filename, index=True,
                                index_label='Id', encoding='utf-8-sig')
        return 'File save successfully!'
    else:
        return 'File already exists!'


response = get_referee_names()
print(response)


def get_bets():
    bet_table = all_data[all_data.columns[23:68]]
    cleared_nan = bet_table.fillna('9999')

    filename = "bet_table.csv"
    files_present = glob.glob(filename)

    if not files_present:
        cleared_nan.to_csv(filename, index=True,
                           index_label='Id', encoding='utf-8-sig')
        return 'File save successfully!'
    else:
        return 'File already exists!'


response = get_bets()
print(response)


def get_games():
    games_table = all_data[all_data.columns[1:23]]
    games_drop_referee = games_table.drop(['Referee'], axis=1)
    cleared_nan = games_drop_referee.fillna('9999')

    club_names = pd.read_csv('club_names.csv')

    cleared_nan['HomeTeam'] = cleared_nan['HomeTeam'].map(
        club_names.set_index('Name')['Id'])
    cleared_nan['AwayTeam'] = cleared_nan['AwayTeam'].map(
        club_names.set_index('Name')['Id'])
    cleared_nan['Date'] = cleared_nan['Date'].replace(['Null'], '01/01/51')
    cleared_nan['Date'] = pd.to_datetime(
        cleared_nan['Date'], errors='coerce', format='%d/%m/%y').dt.strftime('%Y-%m-%d')
    cleared_nan = cleared_nan.fillna(
        {'Date': '1900-01-01', 'HomeTeam': 9999, 'AwayTeam': 9999})
    print(cleared_nan)

    filename = "games_table.csv"
    files_present = glob.glob(filename)

    if not files_present:
        cleared_nan.to_csv(filename, index=True,
                           index_label='Id', encoding='utf-8-sig')
        return 'File save successfully!'
    else:
        return 'File already exists!'


response = get_games()
print(response)
