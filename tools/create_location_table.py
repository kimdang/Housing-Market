import pandas as pd
import translate_state_name
import execute_mysql



# location ID is created from listing dataset 
# state name will be abbreviated
# there are cases where multiple datasets exist for 1 city
listing = pd.read_csv('listing_prices.csv')
listing.drop_duplicates(['RegionName', 'StateName'], keep=False)
new_state = pd.DataFrame(listing['StateName'].map(translate_state_name.state_dictionary))



table_query = "CREATE TABLE location (id INT AUTO_INCREMENT PRIMARY KEY, city VARCHAR(255), state VARCHAR(255))"
execute_mysql.run_query(table_query)



for i in range(listing['RegionName'].count()):
    insert_query = "INSERT INTO location (city, state) VALUES ('%s', '%s')" %(listing['RegionName'][i], new_state['StateName'][i])
    execute_mysql.run_query(insert_query)

