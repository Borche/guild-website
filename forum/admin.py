from django.contrib import admin
from forum.models import Forum, Thread, Comment

# Register your models here.

class ForumAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    
class ThreadAdmin(admin.ModelAdmin):
    list_display = ['headline']
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ['number', 'user']

admin.site.register(Forum, ForumAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Comment, CommentAdmin)