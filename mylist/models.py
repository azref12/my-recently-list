from django.db import models

class kategori (models.Model) :
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100, null=False)

class mylist (models.Model) :
    id_list = models.AutoField(primary_key=True)
    genre_id = models.IntegerField(blank=True, default=0)
    categoryname = models.IntegerField(blank=True, default=0)
    titles = models.CharField(max_length=100, null=False)
    rating = models.IntegerField(blank=True, default=0)