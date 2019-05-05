from django.shortcuts import render

# django rest api
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# class base view
from rest_framework.views import APIView

# @api_view(['GET','POST'])

# def housing_list(request,format=None):
#     if request.method == 'GET':
#         return Response("Hello world", status=status.HTTP_200_OK)
    
#     if request.method == 'POST':
#         return Response("Here is your post request" + request.data, status=status.HTTP_202_ACCEPTED)

class Housing(APIView):
    def get(self, request, format=None):
        return Response("Hello world", status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        return Response(request.data, status=status.HTTP_202_ACCEPTED)