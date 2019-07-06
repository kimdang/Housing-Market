import pandas as pd
import execute_mysql 
import datetime


def prep_data (raw_df, ind):
    city = raw_df.loc[ind,:]
    city = city.T
    city = city.drop(city.index[0:7])
    city = city.dropna().astype(int)
    city = city.to_frame()
    count = city[ind].count()
    date_list = []
    for i in range(count):
        date = datetime.datetime.strptime(city.index[i], "%Y-%m")
        date_list.append(date)
    new_df = pd.DataFrame(city[ind], index=date_list)
    return new_df


homevalue = pd.read_csv('zhvi_allhomes.csv')


for i in range(3):
    city_to_db = prep_data(homevalue, i)
    city_to_db.columns = ['value']
    location_id = i+1

    table_query = "CREATE TABLE data_%s (ind INT AUTO_INCREMENT PRIMARY KEY, dt DATETIME NOT NULL, homevalue INT)" %(location_id)
    execute_mysql.run_query(table_query)

    row_count = city_to_db['value'].count()
    for j in range(row_count):
        insert_query = "INSERT INTO data_%s (dt, homevalue) VALUES ('%s', %s)" %(location_id, city_to_db.index[j], city_to_db['value'][j])
        execute_mysql.run_query(insert_query)