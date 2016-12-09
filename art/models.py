from django.db import models


# Create your models here.

class Picture(models.Model):
    name = models.TextField()
    author = models.TextField()
    price = models.IntegerField()
    materials = models.TextField()
    height = models.IntegerField()
    width = models.IntegerField()
    url = models.URLField()
