import pandas as pd
import translate_state_name
import execute_mysql


# get listing dataset 
listing = pd.read_csv('listing_prices.csv')

# drop duplicates
listing.drop_duplicates(['RegionName', 'StateName'], keep=False, inplace=True)
new_index = pd.Series(range(0, len(listing['RegionName'])))
listing.set_index(new_index, inplace=True)

# state name will be abbreviated
new_state = pd.DataFrame(listing['StateName'].map(translate_state_name.state_dictionary))

# create location table 
table_query = "CREATE TABLE location (id INT AUTO_INCREMENT PRIMARY KEY, city VARCHAR(255), state VARCHAR(255))"
execute_mysql.run_query(table_query)


# for location table, each row is a city
for i in range(listing['RegionName'].count()):
    insert_query = "INSERT INTO location (city, state) VALUES ('%s', '%s')" %(listing['RegionName'][i], new_state['StateName'][i])
    execute_mysql.run_query(insert_query)

