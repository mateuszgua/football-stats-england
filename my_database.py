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
        try:
            config = {
                'user': self.user,
                'password': self.password,
                'host': self.host,
                'port': self.port,
                'database': self.database
            }
            self.connection = msql.connect(**config)
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except Error as e:
            self.connection = None
            self.cursor = None
            print("Error while connecting to MySQL", e)

        else:
            print("Connection created successfully.")
            return self.connection

    def close_connection(self):
        if self.connection:
            self.connection.close()

    def is_connection_valid(self):
        return self.connection and self.connection.is_closed == 0

    def sql_execute(self, sql_execute):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(sql_execute)
        connection.close()

    def sql_execute_many(self, sql_execute, list_execute):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.executemany(sql_execute, list_execute)
        connection.close()

    def sql_get_all_1(self, sql_execute):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(sql_execute)
        result = cursor.fetchall()
        connection.close()
        return result

    def sql_get_one_1(self, sql_execute):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(sql_execute)
        result = cursor.fetchone()
        connection.close()
        return result

    def sql_call_procedure_1(self, proc_name, args):
        connection = self.get_connection()
        cursor = connection.cursor()
        result_args = cursor.callproc(proc_name, args)
        connection.close()
        return result_args
