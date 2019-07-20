import pandas as pd
import datetime
import execute_mysql
import matplotlib.pyplot as plt
import seaborn as sns
from fbprophet import Prophet
import numpy as np
sns.set_style('whitegrid')


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


def get_graph_values (location_id, city, state):
    
    # obtain the dataset of targeted city 
    city_query = "SELECT * FROM data_%s" %(location_id)
    city_df = execute_mysql.run_query(city_query, fetch=True, fetch_option='fetchall')
    city_df = pd.DataFrame(city_df)
    
    # find the start date and end date
    start_dt = city_df.iloc[1,0]
    end_dt = city_df.iloc[-1,0]
    start = "%s-%s-%s" %(start_dt.year,start_dt.month,start_dt.day)
    end = "%s-%s-%s" %(end_dt.year,end_dt.month,end_dt.day)
    
    # all prices will be in thousand 
    city_df['thousand'] = city_df['listing'].divide(1000)

    
    # first graph consists of historical data
    # plt.figure(figsize=(10,5))
    fig1 = sns.lineplot(data=city_df, x='dt', y='thousand')
    fig1.set(xlabel='year', ylabel='US Dollar (thousand)', title='Home Sale Price in %s, %s' %(city, state))
    fig1.figure.savefig('history_%s.png' %(location_id))
    plt.clf()

    
    # second graph will a histogram of percent change
    city_df['percent'] = city_df['thousand'].pct_change()
    fig2 = sns.distplot(city_df['percent'].dropna(), bins=100, color='purple')
    fig2.set(xlabel='Monthly Percent Change', title='Home Sale Price in %s, %s from %s to %s' %(city, state, start,end))
    fig2.figure.savefig('percent_%s.png' %(location_id))
    plt.clf()

    
    # Prophet
    for_model = city_df[['dt', 'thousand']]
    for_model.columns = ['ds','y']
    m = Prophet()
    m.fit(for_model)
    future = m.make_future_dataframe(periods=120, freq='M')
    forecast = m.predict(future)
    
    # calculate 5 and 10 year price
    five_year_dt = "2024-5-31"
    five_year_ind = location.index[(forecast['ds']== five_year_dt).idxmax()]
    five_year_price = forecast['yhat'][five_year_ind]
    ten_year_price = forecast['yhat'].iloc[-1]
    
    # third graph 
    forecast.set_index('ds', inplace=True)
    fig3 = forecast['yhat'].plot(legend=True,label='forecast prices', color='red')
    graph_hist = city_df[['dt', 'thousand']]
    graph_hist.columns = ['dt', 'historical prices']
    graph_hist.set_index('dt', inplace=True)
    graph_hist.plot(style=".", ax=fig3, color='green')
    fig3.set(xlabel='year', ylabel='US Dollar (thousand)', title='Home Sale Price in %s, %s' %(city, state))
    fig3.figure.savefig('predict_%s.png' %(location_id))
    plt.clf()
    
    # calculate values 
    pct_avg = city_df['percent'].mean()
    standard = city_df['percent'].std()

    return pct_avg, standard, five_year_price, ten_year_price
