import mysql.connector
from mysql.connector import connect, Error
from decouple import config

def crete_connection():
    try:
        with connect(**configValue) as connection:
            return mysql.connector.connect
    except Error as e:
    print(e)