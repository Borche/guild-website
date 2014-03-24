from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Forum(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    
    class Meta:
        ''' Ugly solution to the ordering in admin interface '''
        verbose_name_plural = "  Forums" 
        
    def __unicode__(self):
        return self.name
    
class Thread(models.Model):
    user = models.ForeignKey(User)
    forum = models.ForeignKey(Forum)
    headline = models.CharField(max_length=64)
    numOfPosts = models.IntegerField(default=0)
    
    class Meta:
        verbose_name_plural = " Threads"
        
    def __unicode__(self):
        return self.headline

class Comment(models.Model):
    user = models.ForeignKey(User)
    thread = models.ForeignKey(Thread)
    text = models.TextField()
    datetime = models.DateTimeField()
    number = models.IntegerField()
    numOfEdits = models.IntegerField(default=0)
    lastEdited = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Comments"
