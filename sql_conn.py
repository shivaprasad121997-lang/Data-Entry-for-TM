import mysql.connector
from mysql.connector import Error
import sys


def get_my_sql_conn():
    connection = mysql.connector.connect(
            host='127.0.0.1',    # Or 'localhost'
            user='root',         # Default username
            password='Shivaprasad@0',         # Default is often empty
            port=3306,            # Default MySQL port
            database="sys" 
        )
    if connection.is_connected():
        print(f"Successfully connected to MySQL Server version from get conn ")
        return connection
    else:
        print("connection failed in get sql conn")
        sys.exit(1)

def execute_sql_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(list(row))