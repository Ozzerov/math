from django.db import models


# Create your models here.

class Theme(models.Model):
    order = models.IntegerField()
    subject = models.CharField(max_length=16)
    theme = models.CharField(max_length=32)


class Formula(models.Model):
    order = models.IntegerField()
    subject = models.CharField(max_length=16)
    theme = models.CharField(max_length=32)
    formula = models.TextField()
    comment = models.TextField()
