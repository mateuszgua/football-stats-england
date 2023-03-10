from my_database import MyDatabase


class DatabaseReader:

    def __init__(self) -> None:
        self.my_db = MyDatabase()

    def get_all_referee(self):
        cursor = self.my_db.get_cursor()
        sql_select = """SELECT * FROM football_eng.referee"""
        cursor.execute(sql_select)
        result = cursor.fetchall()
        return result
