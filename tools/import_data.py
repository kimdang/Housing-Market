#################
#   Script for importing data from csv file to database
#   Creator: Kim Dang
#   Date: April 7, 2019
#   Version: 1.0
#################

import pandas as pd
import sqlalchemy as sqlal

# path to the data file 
filename = ""
city = pd.read_csv(filename)

city.info()

# mysql://<username>:<password>@<host>/<database>
username = ""
password = ""
host = ""
database = ""
engine = sqlal.create_engine("mysql://" + username + ":" + password + "@" + host + "/" + database)
con = engine.connect()
city.to_sql(name='table_name',con=con,if_exists='append')
con.close()