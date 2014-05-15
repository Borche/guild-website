from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'guild.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', include('news.urls', namespace="news")),
    url(r'^forum/', include('forum.urls', namespace="forum")),
    url(r'^roster/', include('roster.urls', namespace="roster")),
	url(r'^news/', include('news.urls', namespace="news")),
	url(r'^recruitment/', include('recruitment.urls', namespace="recruitment")),
	url(r'^captcha/', include('captcha.urls')), 
    url(r'^admin/', include(admin.site.urls)),
	url(r'^login/$', views.my_login, name='my_login'),
	url(r'^logout/$', views.my_logout, name='my_logout'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
