
import pandas as pd
import execute_mysql 
import translate_state_name
import my_tools


pull_query = "SELECT * FROM location"
location = execute_mysql.run_query(pull_query, fetch=True, fetch_option='fetchall')
location = pd.DataFrame(location)


listing = pd.read_csv('listing_prices.csv')
new_state = pd.DataFrame(listing['StateName'].map(translate_state_name.state_dictionary))
city_count = listing['RegionName'].count()


for i in range(city_count):
    city = listing['RegionName'][i]
    state = new_state['StateName'][i]
    location_id = location.loc[((location['city']==city) & (location['state']==state)).idxmax(),'id']
    # locate the correct location_id of each city 

    
    table_query = "CREATE TABLE data_%s (id INT AUTO_INCREMENT PRIMARY KEY, dt DATETIME NOT NULL, listing INT)" %(location_id)
    execute_mysql.run_query(table_query)
    # each table is named data_<location_id>
    

    city_to_db = my_tools.prep_data(listing, i, drop_column=4)
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

    insert_query = "INSERT INTO data_%s (dt, listing) VALUES %s" %(location_id, total)
    execute_mysql.run_query(insert_query) 
    
