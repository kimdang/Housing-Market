from django.shortcuts import render

# django rest api
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# class base view
from rest_framework.views import APIView


import pymysql.cursors
import DATABASE

HOST = DATABASE.DB_CREDENTIALS['HOST']
USER = DATABASE.DB_CREDENTIALS['USER']
PASSWORD = DATABASE.DB_CREDENTIALS['PASSWORD']
DB = DATABASE.DB_CREDENTIALS['NAME']


# @api_view(['GET','POST'])

# def housing_list(request,format=None):
#     if request.method == 'GET':
#         return Response("Hello world", status=status.HTTP_200_OK)
    
#     if request.method == 'POST':
#         return Response("Here is your post request" + request.data, status=status.HTTP_202_ACCEPTED)

class Housing(APIView):
    def get(self, request, state, city, format=None):
        # you will have state and city name
        # you need to
        # 1. Make connection to database - using mysql pip package
        # 2. Query database with the state and city name
        # 3. if the state and city are in database -> return Response(city, status=status.HTTP_200_OK)
        # 4. if not -> return Response('Not Found', status=status.HTTP_404_NOT_FOUND)
        conn = pymysql.connect(host=HOST,
                             user=USER,
                             password=PASSWORD,
                             db=DB,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

        with conn.cursor() as cursor:
            print(city)
            print(state)
            query1 = "SELECT ind FROM location_id WHERE (city = '%s' AND state = '%s')" %(city, state)
            cursor.execute(query1)
            location_ind = cursor.fetchone()['ind']
            print(location_ind)
            conn.commit()

            if location_ind == None:
                return Response('Not Found', status=status.HTTP_404_NOT_FOUND)
            
            query2 = "SELECT url FROM analysis WHERE location_id = %s" %(location_ind)
            cursor.execute(query2)
            url = cursor.fetchone()['url']
            print(url)
            conn.commit()

            if url == None:
                return Response('Analysis Not Found', status=status.HTTP_404_NOT_FOUND)


            city_info = {
                'id' : location_ind,
                'city' : city,
                'state' : state,
                'figure' : url
            }

  
            return Response(city_info, status=status.HTTP_200_OK)




        print("You entered " + state)
        print("You entered " + city)
        return Response(city, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        return Response(request.data, status=status.HTTP_202_ACCEPTED)