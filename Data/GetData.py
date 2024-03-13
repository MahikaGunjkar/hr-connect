#import cur
import psycopg2
import os

'''def get_db_connection():
    conn = psycopg2.connect(
        host="org-hrconnect-inst-textbook.data-1.use1.tembo.io",
        database="postgres",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])
    return conn

    
import sqlite3

def get_data_from_table():
    connection = sqlite3.connect("org-hrconnect-inst-textbook.data-1.use1.tembo.io")
    cursor = connection.cursor()
    #cursor.execute('SELECT  FROM my_table')
    data = cursor.fetchall()
    connection.close()
    return data
'''

from app import curr

if __name__ == "__main__":
    table_data = curr()
    print(table_data)

