# for each city table, add a column called listing 
# insert data into rows with corresponding datetime 


import pandas as pd
import execute_mysql 
import translate_state_name
import my_tools



pull_query = "SELECT * FROM location_id"
location = execute_mysql.run_query(pull_query, fetch=True, fetch_option='fetchall')
location = pd.DataFrame(location)



listing = pd.read_csv('listing_prices.csv')
new_state = pd.DataFrame(listing['StateName'].map(translate_state_name.state_dictionary))
city_count = listing['RegionName'].count()


for i in range(1): # <------ change to city_count
    city = listing['RegionName'][i]
    state = new_state['StateName'][i]
    location_id = location.loc[((location['city']==city) & (location['state']==state)).idxmax(),'ind']
    # locate the correct location_id of each city 

    city_to_db = my_tools.prep_data(listing, i, drop_column=4)
    city_to_db.columns = ['price']
    entry_count = city_to_db['price'].count()
    
    column_query = "ALTER TABLE data_%s ADD listing INT" %(location_id)
    execute_mysql.run_query(column_query)

    for j in range(entry_count):
        insert_query = "UPDATE data_%s SET listing = %s WHERE dt = '%s'" %(location_id, city_to_db['price'][j], city_to_db.index[j])
        execute_mysql.run_query(insert_query)
    
