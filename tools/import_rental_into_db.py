# for each city table, add a column called rental 
# insert data into rows with corresponding datetime 

import pandas as pd
import execute_mysql 
import translate_state_name
import my_tools


pull_query = "SELECT * FROM location"
location = execute_mysql.run_query(pull_query, fetch=True, fetch_option='fetchall')
location = pd.DataFrame(location)

rental = pd.read_csv('rental_prices.csv')
city_count = rental['RegionName'].count()


for i in range(city_count): 
    city = rental['RegionName'][i]
    state = rental['State'][i]
    location_id = location.loc[((location['city']==city) & (location['state']==state)).idxmax(),'id']
    # locate the correct location_id of each city 

    
    column_query = "ALTER TABLE data_%s ADD rental INT" %(location_id)
    execute_mysql.run_query(column_query)
    # add column named rental into existing table 
    
    city_to_db = my_tools.prep_data(rental, i, drop_column=5)
    city_to_db.columns = ['price']
    row_count = city_to_db['price'].count()

    total = ""
    for j in range(row_count):
        if (j != (row_count-1)):
                one_entry = "('%s',%s)," %(city_to_db.index[j], city_to_db['price'][j])
        else:
                one_entry = "('%s',%s)" %(city_to_db.index[j], city_to_db['price'][j])
        total = total + one_entry
    # create 1 large string for insertion of all entries into 1 city/table  

    insert_query = "INSERT INTO data_%s (dt, rental) VALUES %s" %(location_id, total)
    execute_mysql.run_query(insert_query) 