from django.shortcuts import render

# django rest api
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# class base view
from rest_framework.views import APIView

from execute_mysql import run_query

# @api_view(['GET','POST'])

# def housing_list(request,format=None):
#     if request.method == 'GET':
#         return Response("Hello world", status=status.HTTP_200_OK)
    
#     if request.method == 'POST':
#         return Response("Here is your post request" + request.data, status=status.HTTP_202_ACCEPTED)

class Housing(APIView):
    def get(self, request, state, city, format=None):

        if "_" in city:
            city = city.replace("_", " ")

        query1 = "SELECT id FROM location WHERE (city = '%s' AND state = '%s')" %(city, state)
        location = run_query(query1, fetch=True, fetch_option='fetchone')
        location_id = location['id']

        if location_id == None:
            return Response('Not Found', status=status.HTTP_404_NOT_FOUND)

        query2 = "SELECT * FROM analysis_figure WHERE location_id = %s" %(location_id)
        analysis_figure = run_query(query2, fetch=True, fetch_option='fetchone')
        url_historical = analysis_figure['historical_url']
        url_predict = analysis_figure['predict_url']
        url_pct = analysis_figure['pct_change_url']


        query3 = "SELECT * FROM analysis_value WHERE location_id = %s" %(location_id)
        analysis_val = run_query(query3, fetch=True, fetch_option='fetchone')
        val_5_yr = analysis_val['five_year']
        val_10_yr = analysis_val['ten_year']
        std = analysis_val['std']
        pct_avg = analysis_val['pct_avg']



        city_info = {
            'city' : city,
            'state' : state,
            'location_id' : location_id,
            'historical_data' : url_historical,
            'forecast' : url_predict,
            'histogram' : url_pct,
            '5_year_price' : val_5_yr,
            '10_year_price' : val_10_yr,
            'percent_average' : pct_avg,
            'standard_deviation' : std
        }

  
        return Response(city_info, status=status.HTTP_200_OK)

    
    def post(self, request, format=None):
        return Response(request.data, status=status.HTTP_202_ACCEPTED)