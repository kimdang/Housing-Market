

import pymysql.cursors
import credential
import pandas as pd

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

# PULL RAW DATA zillow_by_city FROM DATABASE
zillow_by_city = pd.read_sql("SELECT * FROM zillow_by_city", con=conn)
location = zillow_by_city[['index', 'RegionName', 'State']]

# CREATE TABLE location_id IN DATABASE
with conn.cursor() as cursor:
    table_query = "CREATE TABLE location_id (ind INT AUTO_INCREMENT PRIMARY KEY, city VARCHAR(255), state VARCHAR(255))"
    cursor.execute(table_query)
    print('Table created.')

for i in range(location['index'].count()):
    with conn.cursor() as cursor:
        insert_query = "INSERT INTO location_id (city, state) VALUES (%s, %s)"
        val = (location['RegionName'][i], location['State'][i])
        cursor.execute(insert_query, val)
        conn.commit()    
        print('Insertion completed.')

# Close connection
conn.close()

