from django.shortcuts import render
import datetime 
from codecs import ignore_errors
from functools import partial
from inspect import isfunction
from re import X

from django.db import DatabaseError, transaction
from django.db.models.aggregates import Max
from django.db.utils import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils import translation
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

t = datetime.datetime.now()

@csrf_exempt
@api_view(["GET"])
@permission_classes([AllowAny])
def Search_Genre (request,  *args, **kwargs) :
    
    if request.method == 'GET':
        try :
            x = request.GET['id']
            ModelList = list (genre.objects.all().extra(select={
                "id_genre" : 'genre_genre.id',
                "genre" : 'genre_genre.genre'},
            tables=['genre_genre'], 
            where=['id='+x]).values('id_genre','genre'))
            
            formater = {
                "mylist" : ModelList
            }
            
            return JsonResponse({'message' : 'successfully', 'results' : formater})
        except :
            return Response(status=status.HTTP_404_NOT_FOUND)
