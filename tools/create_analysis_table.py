import credential
import pymysql.cursors

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

with conn.cursor() as cursor:
    query = "CREATE TABLE analysis (id INT, url VARCHAR(255), location_id INT)"
    cursor.execute(query)
    print("Table created.")

conn.close()