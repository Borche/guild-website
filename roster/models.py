from django.db import models

# Create your models here.

class Character(object):
    name = models.CharField(max_length=32)
    level = models.IntegerField()
    xclass = models.CharField()
    race = models.CharField()
    