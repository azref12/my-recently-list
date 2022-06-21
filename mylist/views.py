# from django.shortcuts import render
# import datetime 
# from codecs import ignore_errors
# from functools import partial
# from inspect import isfunction
# from re import X

# from django.db import DatabaseError, transaction
# from django.db.models.aggregates import Max
# from django.db.utils import IntegrityError
# from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render
# from django.utils import translation
# from django.views.decorators.csrf import csrf_exempt
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import status
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.parsers import JSONParser
# from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
# from rest_framework.renderers import JSONRenderer
# from rest_framework.views import APIView
# from rest_framework.response import Response

# from .models import *
# from .serializers import *

# t = datetime.datetime.now()

# @csrf_exempt
# @api_view(["GET"])
# @permission_classes([AllowAny])
# def My_List (request,  *args, **kwargs) :
    
#     if request.method == 'GET':
#         try :
#             ModelList = list (movies.objects.all().extra(select={
#                 "id_movies" : 'movies_movies.id',
#                 "movies_title" : 'movies_movies.movies_title',
#                 "id_genre" : 'movies_movies.id_genre'},
#             tables=['movies_movies'], 
#             where=['id='+x]).values('id_movies','movies_title','id_genre'))
            
#             formater = {
#                 "mylist" : ModelList
#             }
            
#             return JsonResponse({'message' : 'successfully', 'results' : formater})
#         except :
#             return Response(status=status.HTTP_404_NOT_FOUND)
