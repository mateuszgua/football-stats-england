from my_database import MyDatabase


class DatabaseFillTables:

    def __init__(self) -> None:
        self.my_db = MyDatabase()

# TODO Dodać sprawdzenie czy dane istnieja w bazie, jezeli nie to wykonać ponizsze

    def get_all_referee(self):
        cursor = self.my_db.get_cursor()

        sql = """INSERT INTO referee VALUES (%s, %s)"""
        referee_data = referee_data.drop(columns=['Id'])
        referee_list = referee_data.to_records().tolist()
        cursor.executemany(sql, referee_list)

        sql = """INSERT INTO teams VALUES (%s, %s)"""
        club_data = club_data.drop(columns=['Id'])
        club_list = club_data.to_records().tolist()
        cursor.executemany(sql, club_list)

        sql = """INSERT INTO games VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        games_data = games_data.drop(columns=['Id'])
        games_list = games_data.to_records().tolist()
        cursor.executemany(sql, games_list)

        sql = """INSERT INTO football_eng.bets VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        bet_data = bet_data.drop(columns=['Id'])
        bet_list = bet_data.to_records().tolist()
        cursor.executemany(sql, bet_list)
