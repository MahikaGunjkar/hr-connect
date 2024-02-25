import psycopg2
#import CreateData
#import RatingScale
from dotenv import load_dotenv

# Read data from the table into a DataBase

load_dotenv()

# Open a cursor to perform database operations

def main():
    # Connection string
    conn_str = 'postgresql://postgres:mOHkv8quPBEygqI9@org-hrconnect-inst-textbook.data-1.use1.tembo.io:5432/postgres'
    try:
        # Create a new database session
        conn = psycopg2.connect(conn_str)
    except Exception as e:
        print(f"Unable to connect to the database: {e}")

    try:
        # Create a new cursor object.
        cur = conn.cursor()

        cur.execute('create table Employees (EmpId PRIMARY KEY,'
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
        #Query

        A = cur.execute("select SatA from Employees")
        B = cur.execute("select SunA from Employees")
        C = cur.execute("select SatK from Employees")
        D = cur.execute("select SatH from Employees")
        E = cur.execute("select WLA from Employees")
        F = cur.execute("select WLB from Employees")
        G = cur.execute("select WLC from Employees")
        H = cur.execute("select REL from Employees")
        I = cur.execute("select REW from Employees")
        J = cur.execute("select REE from Employees")
 
        for index, row in df.iterrows():
            for column in df.columns:
                scale = row[column]
                print(f'Cell value at row {index}, column {column}: {scale}')
                


        # Fetch result
        output = cur.fetchone()[0]
        print(output)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close communication with the database
        cur.close()
        conn.close()

if __name__ == "__main__":
    main()
    