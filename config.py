import os

from dotenv import load_dotenv
from os import path

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    USERNAME = os.getenv('MYSQL_USERNAME')
    PASSWORD = os.getenv('MYSQL_PASSWORD')
    HOST = os.getenv('MYSQL_HOST')
    DB_NAME = os.getenv('MYSQL_DB_NAME')
