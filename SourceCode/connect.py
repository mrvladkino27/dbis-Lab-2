import psycopg2
from config import config

def connect():
    print('Connecting to the PostgreSQL database...')
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        # conn = psycopg2.connect("dbname=ZNO_RESULTS user=postgres password=123456789")
        print("CONNECTED")
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def disconnect(conn):
    conn.close()
    print('DISCONNECTED')

def cycle_connect():
    conn = None
    print("Connecting")
    for i in range(5):
        try:
            # read connection parameters
            params = config()
            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            conn.autocommit = True
            return 0
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            continue
    return -1