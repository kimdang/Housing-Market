import credential 
import pymysql

HOST = credential.credentials['host']
USER = credential.credentials['username']
PASSWORD = credential.credentials['password']
DB = credential.credentials['name']

conn = pymysql.connect(host=HOST, 
                       user=USER, 
                       password=PASSWORD, 
                       db=DB, 
                       charset='utf8mb4', 
                       cursorclass=pymysql.cursors.DictCursor)

def run_query (query):
    print(query)
    with conn.cursor() as cursor:
        cursor.execute(query)
        conn.commit()
    return
