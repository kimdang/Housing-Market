import credential
import aws_access
import pymysql
import matplotlib.pyplot as plt
import pandas as pd
import boto3
from botocore.client import Config
import os

def get_url (ind):
    city_df = zillow_by_city.loc[ind,:]
    city_df = city_df.T
    city_df = city_df.drop(city_df.index[0:7])
    
    filename = str(ind)
    fig = city_df.plot()
    fig.set_title('%s,%s' %(zillow_by_city['RegionName'][ind], zillow_by_city['State'][ind]) )
    fig.set_ylabel('US dollar')
    fig.figure.savefig('%s.png' %(filename))
    
    data = open('%s.png' %(filename), 'rb')
    s3.Bucket(BUCKET_NAME).put_object(Key='%s.png' %(filename), Body=data, ContentType = 'image/png')
    link = "https://" + BUCKET_NAME + ".s3-us-west-2.amazonaws.com/" + filename + ".png"
    
    plt.clf()
    os.remove('%s.png' %(filename))
    return link

#ESTABLISH CONNECTION TO DATABASE
HOST = credential.credentials['host']
USER = credential.credentials['username']
PASSWORD = credential.credentials['password']
DB = credential.credentials['name']

conn = pymysql.connect(host=HOST, 
                       user=USER, 
                       password=PASSWORD, 
                       db=DB, 
                       charset='utf8mb4', 
                       cursorclass=pymysql.cursors.DictCursor)

#ESTABLISH CONNECTION TO S3 BUCKET
ACCESS_KEY_ID = aws_access.access['ACCESS_KEY_ID']
ACCESS_SECRET_KEY = aws_access.access['ACCESS_SECRET_KEY']
BUCKET_NAME = aws_access.access['BUCKET_NAME']

s3 = boto3.resource('s3',
                   aws_access_key_id = ACCESS_KEY_ID, 
                   aws_secret_access_key = ACCESS_SECRET_KEY,
                   config = Config(signature_version='s3v4'))

# IMPORT RAW DATA FROM DATABASE
table_name = "zillow_by_city"
zillow_by_city = pd.read_sql('SELECT * FROM %s' %(table_name), con=conn)
max_ind = zillow_by_city['index'].count()

#CALL get_url() 
i = 0
for i in range(max_ind):
    url = get_url(i)
    with conn.cursor() as cursor:
        insert_sql = "INSERT INTO analysis (url, location_id) VALUES (%s, %s)"
        val = (url, i+1)
        cursor.execute(insert_sql, val)
        conn.commit()
        print('Insertion completed for %s, %s' %(zillow_by_city['RegionName'][i], zillow_by_city['State'][i]))

conn.close()