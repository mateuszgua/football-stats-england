import os
import glob
import pandas as pd
import numpy as np

os.chdir("./data")

all_data = pd.read_csv('append_files.csv')
# print(all_data)


def get_club_names():
    df = all_data['HomeTeam'].unique()
    df_club_names = pd.DataFrame(df, columns=['Name'])

    filename = "club_names.csv"
    files_present = glob.glob(filename)

    if not files_present:
        df_club_names.to_csv(filename, index=True,
                             index_label='Id', encoding='utf-8-sig')
        return 'File save successfully!'
    else:
        return 'File already exists!'


response = get_club_names()
# print(response)


def get_referee_names():
    df = all_data['Referee'].unique()
    df_referee_names = pd.DataFrame(df, columns=['Name'])

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
    # df_referee_names = pd.DataFrame(bet_table, columns=['Name'])

    filename = "bet_table.csv"
    files_present = glob.glob(filename)

    if not files_present:
        bet_table.to_csv(filename, index=True,
                         index_label='Id', encoding='utf-8-sig')
        return 'File save successfully!'
    else:
        return 'File already exists!'


response = get_bets()
print(response)


def get_games():
    df = all_data[all_data.columns[1:23]]
    df2 = df.drop(['Referee'], axis=1)

    filename = "games_table.csv"
    files_present = glob.glob(filename)

    if not files_present:
        df2.to_csv(filename, index=True,
                   index_label='Id', encoding='utf-8-sig')
        return 'File save successfully!'
    else:
        return 'File already exists!'


response = get_games()
print(response)
