from django.db import models


# Create your models here.

class Subject(models.Model):
    order = models.IntegerField()
    subject = models.CharField(max_length=16)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ('order',)


class Theme(models.Model):
    order = models.IntegerField()
    subject = models.ForeignKey(Subject)
    theme = models.CharField(max_length=16)

    def __str__(self):
        return "%s > %s" % (self.subject, self.theme)

    class Meta:
        ordering = ('order',)


class Formula(models.Model):
    order = models.IntegerField()
    theme = models.ForeignKey(Theme)
    header = models.CharField(max_length=32, null=True)
    formula = models.TextField()

    class Meta:
        ordering = ('order',)
