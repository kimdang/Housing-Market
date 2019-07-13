import pandas as pd
import translate_state_name
import my_tools
import execute_mysql


listing = pd.read_csv('listing_prices.csv')
new_state = pd.DataFrame(listing['StateName'].map(translate_state_name.state_dictionary))

table_query = "CREATE TABLE location (id INT AUTO_INCREMENT PRIMARY KEY, city VARCHAR(255), state VARCHAR(255))"
execute_mysql.run_query(table_query)


for i in range(listing['RegionName'].count()):
    insert_query = "INSERT INTO location (city, state) VALUES ('%s', '%s')" %(listing['RegionName'][i], new_state['StateName'][i])
    execute_mysql.run_query(insert_query)