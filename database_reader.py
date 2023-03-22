from config import Config
from my_database import MyDatabase


class DatabaseReader:

    def __init__(self) -> None:
        self.db = MyDatabase()

    def get_all_referee(self):
        sql_select = f"""SELECT * FROM {Config.DB_NAME}.referee"""
        result = self.db.sql_get_all_1(sql_select)
        return result

    def is_table_not_empty(self, table_name) -> bool:
        sql_select = f"""SELECT COUNT(*) FROM {Config.DB_NAME}.{table_name}"""
        result = self.db.sql_get_one_1(sql_select)
        table_exist = result[0]
        if table_exist != 0:
            return True
        else:
            return False
