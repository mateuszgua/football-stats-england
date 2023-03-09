import os
import glob
import pandas as pd

os.chdir("./data")


def append_all_files():
    csv_files = glob.glob('*.{}'.format('csv'))
    df_append = pd.DataFrame()

    for file in csv_files:
        df_temp = pd.read_csv(file, encoding='utf-8')
        df_append = df_append.append(df_temp, ignore_index=True)

    filename = "append_files.csv"
    files_present = glob.glob(filename)

    if not files_present:
        df_append.to_csv(filename, index=False, encoding='utf-8-sig')
        return 'File save successfully!'
    else:
        return 'File already exists!'


response = append_all_files()
print(response)
