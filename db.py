import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        conn = mysql.connector.connect(
            host='127.0.0.1:3306',
            user='root',
            password='root',
            database='OuterWilds'
        )
        return conn
    except Error as e:
        print("Erro na conexão:", e)
        return None