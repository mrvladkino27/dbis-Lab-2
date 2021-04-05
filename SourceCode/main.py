import psycopg2
import csv
import connect
import SQLScripts
from time_counter import profile_time

#section for working with DB
@profile_time
def create_table(drop_table, conn):
    print('Start table creation')
    cur = conn.cursor()
    if not (drop_table):
        cur.execute(SQLScripts.delete_tables)
        conn.commit()
    cur.execute(SQLScripts.create_normal_form_tables)
    conn.commit()
    cur.close()
    print('End table creation')
    

#Migrating data from znodata to new tables
@profile_time
def migrate_data(conn): 
    print('Start migration')  
      
    cur = conn.cursor()
    cur.execute(SQLScripts.migrate_data_in_db)
    conn.commit()
    cur.close()
    
    print('End migration')

#Executing querry and save results
@profile_time
def get_max_eng_2019_2020(conn):
    print('Start querry executing')
    with conn.cursor() as cursor:
        cursor.execute(SQLScripts.query)
        print('End querry executing')
        rows = cursor.fetchall()         
    header = ['Results',"Year"]
    with open('Results/QueryResult.csv', 'w') as result:
        result_writer = csv.writer(result, delimiter=';')
        result_writer.writerow(header)
        for line in rows:
            result = []
            for elem in line:
                result.append(int(elem))
            result_writer.writerow(result)

def print_console_line():
    print("\n=====================================================================================================================\n")

if __name__ == '__main__':
    conn = connect.connect()
    print_console_line()
    create_table(1,conn)
    print_console_line()
    migrate_data(conn)
    print_console_line()
    get_max_eng_2019_2020(conn) 
    print_console_line()
    connect.disconnect(conn)