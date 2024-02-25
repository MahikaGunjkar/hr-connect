import psycopg2
#import CreateData
#import RatingScale

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

        cur.execute("create table users (user_id int, password varchar)")
        cur.execute("select John from CreateData")
        # Test Query
        cur.execute("SELECT 1")

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
    