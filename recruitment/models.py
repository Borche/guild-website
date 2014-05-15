from django.db import models
from django.utils import timezone

# Create your models here.
class Application(models.Model):
    character_name = models.CharField(max_length=30)
    email = models.EmailField()
    race = models.CharField(max_length=9)
    xclass = models.CharField(max_length=12)
    level = models.IntegerField(default=90)
    item_level = models.IntegerField(default=1)
    message = models.TextField(max_length=10000)
    date = models.DateTimeField('Date of application', default=timezone.now)
    header = models.CharField(max_length=100, default=character_name)
	