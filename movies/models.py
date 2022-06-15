from django.db import models

class movies (models.Model) :
    id = models.AutoField(primary_key=True)
    movies_title = models.CharField(max_length=100, null=False)
    id_genre = models.IntegerField(blank=True, default=0)
