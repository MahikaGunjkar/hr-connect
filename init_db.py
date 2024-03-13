'''
import os
import psycopg2
# from dotenv import load_dotenv

#load_dotenv()

conn = psycopg2.connect(
        host="org-hrconnect-inst-textbook.data-1.use1.tembo.io",
        database="postgres",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS Employees;')
cur.execute('CREATE TABLE Employees (EmpId PRIMARY KEY,'
                                 ' SatA INT,'
                                 ' SunA INT,' 
                                 ' SatK INT, '
                                 ' SatH INT,' 
                                 ' SatS INT,'
                                 ' WLA INT, ' 
                                 ' WLB INT,'
                                 ' WLC INT,' 
                                 ' REL INT,' 
                                ' REW INT,'
                                ' REE INT);'
                                 )

conn.commit()
cur.close()
conn.close() 
'''