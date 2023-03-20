from views import app as application
from database_manager import DatabaseManager
from database_fill_tables import DatabaseFillTables

if __name__ == '__main__':
    with application.app_context():
        application.config.from_object('config.DevelopmentConfig')
        init_db = DatabaseManager()
        init_files = DatabaseFillTables()
        init_db.create_database()
        init_db.create_tables()
        init_files.get_csv_files()
    application.run()
