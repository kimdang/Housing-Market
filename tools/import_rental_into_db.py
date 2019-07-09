# for each city table, add a column called listing 
# insert data into rows with corresponding datetime 

import pandas as pd
import execute_mysql 
import translate_state_name
import my_tools


pull_query = "SELECT * FROM location_id"
location = execute_mysql.run_query(pull_query, fetch=True, fetch_option='fetchall')
location = pd.DataFrame(location)

rental = pd.read_csv('rental_prices.csv')
city_count = rental['RegionName'].count()


for i in range(1): # change to city_count 
    city = rental['RegionName'][i]
    state = rental['State'][i]
    location_id = location.loc[((location['city']==city) & (location['state']==state)).idxmax(),'ind']
    # locate the correct location_id of each city 


    city_to_db = my_tools.prep_data(rental, i, drop_column=5)
    city_to_db.columns = ['price']
    entry_count = city_to_db['price'].count()
    
    column_query = "ALTER TABLE data_%s ADD rental INT" %(location_id)
    execute_mysql.run_query(column_query)

    for j in range(entry_count):
        insert_query = "UPDATE data_%s SET rental = %s WHERE dt = '%s'" %(location_id, city_to_db['price'][j], city_to_db.index[j])
        execute_mysql.run_query(insert_query)