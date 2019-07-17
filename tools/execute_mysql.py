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

def run_query (query, fetch=False, fetch_option='fetchone'):
    print(query)
    with conn.cursor() as cursor:
        cursor.execute(query)
        if fetch==True:
            if fetch_option == "fetchone":
                result = cursor.fetchone()
            else:
                result = cursor.fetchall()
        conn.commit()
    if fetch==True:
        return result
    else:
        return    

