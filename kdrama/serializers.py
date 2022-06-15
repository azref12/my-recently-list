from rest_framework import serializers
from .models import *

class KdramaSerializers (serializers.ModelSerializer) :
    
    class Meta : 
        model = kdrama
        # fields = ['id','title','idgenre','date_release']
        fields = "__all__" 