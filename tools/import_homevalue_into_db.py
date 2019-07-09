# create table for each city using dataset homevalue


import pandas as pd
import execute_mysql 
import my_tools



homevalue = pd.read_csv('zhvi_allhomes.csv')
city_count = homevalue['RegionName'].count()



for i in range(2): # <----- change to city_count
    city_to_db = my_tools.prep_data(homevalue, i, drop_column=7)
    city_to_db.columns = ['value']
    location_id = i+1
    # location_id table was created using dataset homevalue
    # location_id start at 1, while index of dataset homevalue start at 0, therefore location_id = index + 1

    table_query = "CREATE TABLE data_%s (ind INT AUTO_INCREMENT PRIMARY KEY, dt DATETIME NOT NULL, homevalue INT)" %(location_id)
    execute_mysql.run_query(table_query)
    # each table is named data_<location_id>


    row_count = city_to_db['value'].count()
    for j in range(row_count):
        insert_query = "INSERT INTO data_%s (dt, homevalue) VALUES ('%s', %s)" %(location_id, city_to_db.index[j], city_to_db['value'][j])
        execute_mysql.run_query(insert_query)