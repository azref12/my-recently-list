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
@api_view(["GET", "POST", "PUT"])
@permission_classes([AllowAny])
def genre_list (request):
    
        mymodels = genre
        myserializer = GenreSerializers

        if request.method == 'GET':
            
                mymodels = genre.objects.all()
                myserializer = GenreSerializers (mymodels, many=True)
                
                return JsonResponse({'message' : 'successfully', 'results' : myserializer.data})
    
        if request.method == 'POST':
            try :
                localrequest = JSONParser().parse(request)
                mastermodel = genre.objects.all()
                masterserializer = myserializer (mastermodel, data=localrequest)
                
                if masterserializer.is_valid():
                        genre_save = genre (
                                            genre = localrequest["genre"]
                                    )
                        genre_save.save()

                        mastermodel = genre.objects.all()
                        masterserializer = myserializer (mastermodel, many=True)
                        
                        return JsonResponse ({'results' : masterserializer.data})
                        
            except genre.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

                
@csrf_exempt
@api_view(["GET", "PUT", "DELETE"])
@permission_classes([AllowAny]) 
def genre_detail (request, pk):
    
        mymodels = genre
        myserializer = GenreSerializers
        
        try:
                localmodel = mymodels.objects.get(id=pk)
        except mymodels.DoesNotExist:
                return HttpResponse(status=404)

        if request.method == 'GET':
        
                localserializer = myserializer(localmodel)
                return JsonResponse(localserializer.data)
    
        elif request.method == 'PUT': 
                localrequest = JSONParser().parse(request) 
                localserializer = myserializer(localmodel, data=localrequest) 

                if localserializer.is_valid(): 
                
                        localserializer.save()  
                
                        localmodel = mymodels.objects.all()
                        localserializer = myserializer(localmodel, many=True)

                        return JsonResponse({'message' : 'successfully' , 'status' : True , 'count' : 1 , 'results' : localserializer.data},
                                        status=201)
                return JsonResponse(localserializer.errors, status=400) 

        elif request.method == 'DELETE': 
                localmodel.delete() 
                localmodel = mymodels.objects.all()
                localserializer = myserializer(localmodel, many=True)

        return JsonResponse({'message' : 'successfully' , 'status' : True , 'count' : 1 , 'results' : localserializer.data},
                                status=201)         

                            
