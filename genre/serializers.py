from rest_framework import serializers
from .models import *

class GenreSerializers (serializers.ModelSerializer) : 
    
    class Meta : 
        model = genre
        # fields = ['id','genre']
        fields = "__all__"