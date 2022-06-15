from django.db import models

class genre (models.Model) :
    id = models.AutoField(primary_key=True)
    genre = models.CharField(max_length=100, null=False)
 