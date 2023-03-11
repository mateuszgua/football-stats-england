import os
import glob
import pandas as pd


class AppendCsvFiles:

    def __init__(self) -> None:
        pass

    def create_full_data_table(self, path):
        os.chdir("../source")
        csv_files = glob.glob('*.{}'.format('csv'))
        df_append = pd.DataFrame()

        for file in csv_files:
            df_temp = pd.read_csv(file, encoding='utf-8')
            df_append = df_append.append(df_temp, ignore_index=True)

        file_exist = glob.glob(path)

        if not file_exist:
            df_append.to_csv(path, index=False, encoding='utf-8-sig')
            return 'File save successfully!'
        else:
            return 'File already exists!'

    def update_full_data_table(self, path):
        if os.path.exists(path):
            os.remove(path)
            self.create_full_data_table(path)
        else:
            print("The file does not exist")
