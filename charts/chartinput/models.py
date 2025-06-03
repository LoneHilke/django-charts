from django.db import models

# Create your models here.
class Data(models.Model):
    month = models.CharField(max_length=50)
    salg = models.FloatField()
    year = models.ManyToManyField('Year', related_name='item')
    def __str__(self):
        return self.month

class Year(models.Model):
    year = models.IntegerField()

    def __int__(self):
      return self.year