from django.db import models

class kdrama (models.Model) :
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False)
    idgenre = models.IntegerField(blank=True, default=0)
    date_release = models.DateTimeField()