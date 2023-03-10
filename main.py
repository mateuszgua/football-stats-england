from database_manager import DatabaseManager

if __name__ == '__main__':
    init_db = DatabaseManager()
    init_db.create_database()
    init_db.create_tables()
