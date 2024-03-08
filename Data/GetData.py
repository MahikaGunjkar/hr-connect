#import cur
import psycopg2
import os

def get_db_connection():
    conn = psycopg2.connect(
        host="org-hrconnect-inst-textbook.data-1.use1.tembo.io",
        database="postgres",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])
    return conn

