#################
#   Script for importing data from csv file to database
#   Creator: Kim Dang
#   Date: April 7, 2019
#   Version: 1.0
#################

import pandas as pd
import sqlalchemy as sqlal

def convert_dollar_to_int ():
    s=sanjose['Single Family Home'].str.replace(",", '')
    a=s.str.lstrip('$')
    c=a.astype('int')
    sanjose['Single Family Home'] = c

def convert_to_datetime ():
    start = datetime.datetime(2000,1,1)
    mylist = []
    ngan = start
    for item in sanjose['Date']:
        mylist.append(ngan)
        ngan = add_months(start,1)
        start = ngan


def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    return datetime.date(year, month, day)


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