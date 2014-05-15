from django.shortcuts import render

from news.models import Article

# Create your views here.
def news(request):
	articles = Article.objects.all().order_by('-pub_date')
	return render(request, 'news/news.html', { 'articles': articles })