from django.db import models


# Create your models here.

class Formula(models.Model):
    subject = models.CharField(max_length=16)
    theme = models.CharField(max_length=32)
    formula = models.TextField()
    comment = models.TextField()
    order = models.FloatField()
