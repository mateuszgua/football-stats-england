import os
import glob
import pandas as pd

os.chdir("./data")

csv_files = glob.glob('*.{}'.format('csv'))
print(csv_files)


df_append = pd.DataFrame()

for file in csv_files:
    df_temp = pd.read_csv(file, encoding='utf-8')
    df_append = df_append.append(df_temp, ignore_index=True)

df_append.to_csv("append_files.csv", index=False, encoding='utf-8-sig')
