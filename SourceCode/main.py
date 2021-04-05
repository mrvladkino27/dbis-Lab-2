import psycopg2
import csv
import connect
import SQLScripts
from settings import profile_time

source_file_start = '../../Lab 1/SourceData/Odata'  # between start and end year will be located. It's importing for running code
source_file_end = 'File.csv'
path_result_time = 'result_time.txt'
path_result_query = 'result_querry.csv'

#-----------------------------------------------
#section for working with DB
#-----------------------------------------------  
@profile_time
def work_with_DB_tables(drop_table, conn):
    print('Start table creation')
    cur = conn.cursor()
    if not (drop_table):
        cur.execute(SQLScripts.delete_tables)
        conn.commit()
    cur.execute(SQLScripts.create_normal_form_tables)
    conn.commit()
    cur.close()
    print('End table creation')
    
#-----------------------------------------------
#creating the temporary file for working with data
#and upload temp file to database
#-----------------------------------------------            


#-----------------------------------------------
#Executing querry and save results
#----------------------------------------------- 
querry = ("""select res2019.regname  as "Region",
        res2019.eng_avg as "English 2019",
        res2020.eng_avg as "English 2020"
    from (select regname, avg(engball100) eng_avg
        from results
        where results.engteststatus = 'Зараховано'
            and results.year = 2019
        group by results.regname) as res2019
            join
        (select regname, avg(engball100) as eng_avg
        from results
        where results.engteststatus = 'Зараховано'
            and results.year = 2020
        group by results.regname) as res2020
        on res2019.regname = res2020.regname
    order by "Region";""")

def do_querry(querry,conn):
    print('Start querry executing')  
      
    cur = conn.cursor()
    cur.execute(querry)
    conn.commit()
    rows = cur.fetchall()
    cur.close()
    
    print('End querry executing')



if __name__ == '__main__':
    conn = connect.connect()
    work_with_DB_tables(0, conn)
    
    connect.disconnect(conn)