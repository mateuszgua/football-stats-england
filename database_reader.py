from config import Config
from my_database import MyDatabase


class DatabaseReader:

    def __init__(self) -> None:
        self.my_db = MyDatabase()

    def get_all_referee(self):
        cursor = self.my_db.get_cursor()
        sql_select = f"""SELECT * FROM {Config.DB_NAME}.referee"""
        cursor.execute(sql_select)
        result = cursor.fetchall()
        return result

    def is_table_not_empty(self, table_name) -> bool:
        cursor = self.my_db.get_cursor()
        sql_select = f"""SELECT COUNT(*) FROM {Config.DB_NAME}.{table_name}"""
        cursor.execute(sql_select)
        result = cursor.fetchone()
        table_exist = result[0]
        if table_exist != 0:
            return True
        else:
            return False
