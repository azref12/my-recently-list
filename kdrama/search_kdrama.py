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
def Search_Kdrama (request,  *args, **kwargs) :
    
    if request.method == 'GET':
        try :
            x = request.GET['id']
            ModelList = list (kdrama.objects.all().extra(select={
                "id_kdrama" : 'kdrama_kdrama.id',
                "kdrama_title" : 'kdrama_kdrama.title',
                "id_genre" : 'kdrama_kdrama.idgenre'},
            tables=['kdrama_kdrama'], 
            where=['id='+x]).values('id_kdrama','kdrama_title','id_genre'))
            
            formater = {
                "mylist" : ModelList
            }
            
            return JsonResponse({'message' : 'successfully', 'results' : formater})
        except :
            return Response(status=status.HTTP_404_NOT_FOUND)
