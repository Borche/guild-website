from django.db import models
from django.utils import timezone

# Create your models here.

class Character(object):
    name = models.CharField(max_length=32)
    level = models.IntegerField()
    xclass = models.CharField()
    race = models.CharField()
    
class JsonData(models.Model):
	description = models.CharField(max_length=32)
	json = models.TextField()
	date = models.DateTimeField('Publish date', default=timezone.now)
	
	def __unicode__(self):
		return self.description + " " + str(self.date)