from rest_framework import serializers
from .models import *

class CategorySerializers (serializers.ModelSerializer) : 
    
    class Meta : 
        model = kategori
        # fields = ['id','category_name']
        fields = "__all__" 

class ListSerializers (serializers.ModelSerializer) : 
    
    class Meta : 
        model = mylist
        # fields = ['id_list','genre_id','categoryname','titles','rating']
        fields = "__all__" 