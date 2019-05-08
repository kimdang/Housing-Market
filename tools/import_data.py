#################
#   Script for importing data from csv file to database
#   Creator: Kim Dang
#   Date: April 7, 2019
#   Version: 1.0
#################

import sqlalchemy as sqlal
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import calendar
%matplotlib inline

def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    return datetime.date(year, month, day)

def convert_dollar_object_to_int(source):
    no_comma = source.str.replace(",", '')
    no_dollar = no_comma.str.lstrip('$')
    complete = no_dollar.astype('int')
    source = complete
    return source

def convert_to_datetime_by_month(source,start_year,start_month,start_day):
    start = datetime.datetime(start_year,start_month,start_day)
    datetime_list = []
    for item in source:
        datetime_list.append(start)
        start = add_months(start,1)
    source = datetime_list
    return source

def extract_from_zillow_by_city (city):
    if any(city in s for s in zillow_by_city['RegionName']):
        ind = zillow_by_city.index[zillow_by_city['RegionName']==city]
        city_df = zillow_by_city.loc[ind,:]
        city_df = city_df.T
        city_df = city_df.drop(city_df.index[0:7])
        city_df.columns = [city]
        return city_df
    else:
        return "Does not exist in databse."


def calculate_moving_average (df):
    MA_day = [14,30,60]
    for MA in MA_day:
        column_name = "MA for %s days" %(str(MA))
        df[column_name] = df['Listing'].rolling(MA).mean()
    return df

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
city.to_sql(name='table_name',con=con,if_exists='replace')
con.close()