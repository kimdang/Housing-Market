
import sqlalchemy as sqlal
import pandas as pd
import sys

import credential
print(credential.credentials['password'])

# Establish connection to housing databse
username = credential.credentials['username']
password = credential.credentials['password']
host = "54.244.202.224"
database = "housing"
engine = sqlal.create_engine("mysql://" + username + ":" + password + "@" + host + "/" + database)
con = engine.connect()

# Pull data from zillow_by_city table
table_name = "zillow_by_city"
zillow_by_city = pd.read_sql('SELECT * FROM %s' %(table_name), con=con)

# Create location table
location = zillow_by_city[['RegionName', 'State']]
location.columns = ['City', 'State']
location.head()

# Create location table
location = zillow_by_city[['RegionName', 'State']]
location.columns = ['City', 'State']
location.head()

# Close connection
con.close()

