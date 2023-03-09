import mysql.connector as msql
from mysql.connector import Error

import config

configuration = config.Config()

try:
    conn = msql.connect(host=configuration.HOST, user=configuration.USERNAME,
                        password=configuration.PASSWORD)

    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE {configuration.DB_NAME}")
        print("Database is created")

except Error as e:
    print("Error while connecting to MySQL", e)
