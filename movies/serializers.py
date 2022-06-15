from rest_framework import serializers
from .models import *

class MoviesSerializers (serializers.ModelSerializer) : 
    
    class Meta : 
        model = movies
        # fields = ['id','movies_title','id_genre']
        fields = "__all__" 