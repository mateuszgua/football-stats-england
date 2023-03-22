import mysql.connector as msql
from mysql.connector import Error

from config import Config


class MyDatabase:

    def __init__(self) -> None:
        self.database = Config.DB_NAME
        self.user = Config.USERNAME
        self.password = Config.PASSWORD
        self.host = Config.HOST
        self.port = Config.PORT
        self.connection = None
        self.cursor = None

    def get_connection(self):
        # if self.is_connection_valid():
        #     return self.connection
        # self.close_connection()

        try:
            self.connection = msql.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database)
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except Error as e:
            self.connection = None
            self.cursor = None
            print("Error while connecting to MySQL", e)

        else:
            print("Connection created successfully.")
            return self.cursor

    def close_connection(self):
        if self.connection:
            self.connection.close()

    def is_connection_valid(self):
        return self.connection and self.connection.is_closed == 0

    # def get_cursor(self):
    #     connection = self.get_connection()
    #     cursor = connection.cursor()
    #     return cursor

    def sql_execute(self, sql_execute):
        self.get_connection()
        # cursor = connection.cursor()
        self.cursor.execute(sql_execute)

    def sql_execute_many(self, sql_execute, list_execute):
        self.get_connection()
        # cursor = connection.cursor()
        self.cursor.executemany(sql_execute, list_execute)

    def sql_get_all(self, sql_execute):
        self.get_connection()
        # cursor = connection.cursor()
        self.cursor.execute(sql_execute)
        result = self.cursor.fetchall()
        return result

    def sql_get_one(self, sql_execute):
        self.get_connection()
        # cursor = connection.cursor()
        self.cursor.execute(sql_execute)
        result = self.cursor.fetchone()
        return result

    def sql_call_procedure(self, proc_name, args):
        self.get_connection()
        # cursor = connection.cursor()
        result_args = self.cursor.callproc(proc_name, args)
        return result_args

    def sql_execute_1(self, sql_execute):
        database = Config.DB_NAME
        user = Config.USERNAME
        password = Config.PASSWORD
        host = Config.HOST
        port = Config.PORT
        connection = None
        cursor = None

        config = {
            'user': 'root',
            'password': 'root',
            'host': 'mysql',
            'port': '3306',
            'database': 'football_eng'
        }
        connection = msql.connect(**config)
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(sql_execute)
        connection.close()
        # self.get_connection()
        # # cursor = connection.cursor()
        # self.cursor.execute(sql_execute)

    def sql_execute_many_1(self, sql_execute, list_execute):
        database = Config.DB_NAME
        user = Config.USERNAME
        password = Config.PASSWORD
        host = Config.HOST
        port = Config.PORT
        connection = None
        cursor = None

        config = {
            'user': 'root',
            'password': 'root',
            'host': 'mysql',
            'port': '3306',
            'database': 'football_eng'
        }
        connection = msql.connect(**config)
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.executemany(sql_execute, list_execute)
        connection.close()

    def sql_get_all_1(self, sql_execute):
        database = Config.DB_NAME
        user = Config.USERNAME
        password = Config.PASSWORD
        host = Config.HOST
        port = Config.PORT
        connection = None
        cursor = None

        config = {
            'user': 'root',
            'password': 'root',
            'host': 'mysql',
            'port': '3306',
            'database': 'football_eng'
        }
        connection = msql.connect(**config)
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(sql_execute)
        result = cursor.fetchall()
        connection.close()
        return result

    def sql_get_one_1(self, sql_execute):
        database = Config.DB_NAME
        user = Config.USERNAME
        password = Config.PASSWORD
        host = Config.HOST
        port = Config.PORT
        connection = None
        cursor = None

        config = {
            'user': 'root',
            'password': 'root',
            'host': 'mysql',
            'port': '3306',
            'database': 'football_eng'
        }
        connection = msql.connect(**config)
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(sql_execute)
        result = cursor.fetchone()
        connection.close()
        return result

    def sql_call_procedure_1(self, proc_name, args):
        database = Config.DB_NAME
        user = Config.USERNAME
        password = Config.PASSWORD
        host = Config.HOST
        port = Config.PORT
        connection = None
        cursor = None

        config = {
            'user': 'root',
            'password': 'root',
            'host': 'mysql',
            'port': '3306',
            'database': 'football_eng'
        }
        connection = msql.connect(**config)
        connection.autocommit = True
        cursor = connection.cursor()
        result_args = cursor.callproc(proc_name, args)
        connection.close()
        return result_args
