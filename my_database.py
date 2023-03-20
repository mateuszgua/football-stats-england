import mysql.connector as msql
from mysql.connector import Error

from config import Config


class MyDatabase:

    def __init__(self) -> None:
        self.database = Config.DB_NAME
        self.user = Config.USERNAME
        self.password = Config.PASSWORD
        self.host = Config.HOST
        self.connection = None

    def get_connection(self):
        if self.is_connection_valid():
            return self.connection
        self.close_connection()

        try:
            self.connection = msql.connect(host=self.host,
                                           user=self.user,
                                           password=self.password,
                                           database=self.database)
            self.connection.autocommit = True

        except Error as e:
            self.connection = None
            print("Error while connecting to MySQL", e)

        else:
            print("Connection created successfully.")

        return self.connection

    def close_connection(self):
        if self.connection:
            self.connection.close()

    def is_connection_valid(self):
        return self.connection and self.connection.is_closed == 0

    def get_cursor(self):
        return self.get_connection().cursor()
