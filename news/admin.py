from django.contrib import admin
from news.models import Article

class ArticleAdmin(admin.ModelAdmin):
	fields = ['header', 'text']
	list_display = ['header']
	
	def save_model(self, request, obj, form, change):
		#if getattr(obj, 'author', None) is None:
		obj.author = request.user
		obj.save()

# Register your models here.
admin.site.register(Article, ArticleAdmin)