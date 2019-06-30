


import credential
import pymysql.cursors

# ESTABLISH CONNECTION TO DATABASE
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

# CREATE TABLE analysis IN DATABASE
with conn.cursor() as cursor:
    query = "CREATE TABLE analysis (ind INT AUTO_INCREMENT PRIMARY KEY, url VARCHAR(255), location_id INT, FOREIGN KEY (location_id) REFERENCES location_id(ind) ON UPDATE CASCADE)"
    cursor.execute(query)
    print("Table created.")

# CLOSE CONNECTION
conn.close()