from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import admin

# Create your models here.
class Article(models.Model):
	author = models.ForeignKey(User)
	pub_date = models.DateTimeField('Publish date', default=timezone.now)
	header = models.CharField(max_length=64)
	text = models.TextField(max_length=20000)
	image = models.ImageField('Article image', upload_to='images/', blank=True, null=True)