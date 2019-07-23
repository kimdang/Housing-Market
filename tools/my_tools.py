import pandas as pd
import datetime


def prep_data (raw_df, ind, drop_column):
    # raw_df : raw data of all cities 
    # ind : index of city to be isolated from raw data 
    # drop_column : the number of column(s), starting from index column, that contains information other than price such as district, rank size, etc.
    # for dataset homevalue, drop_column = 7
    # for dataset listing, drop column = 4
    # for dataset rental, drop column = 5

    city = raw_df.loc[ind,:]
    city = city.T
    city = city.drop(city.index[0:drop_column])
    city = city.dropna().astype(int)
    city = city.to_frame()
    count = city[ind].count()
    date_list = []

    for i in range(count):
        date = datetime.datetime.strptime(city.index[i], "%Y-%m")
        date_list.append(date)
        new_df = pd.DataFrame(city[ind], index=date_list)
    return new_df