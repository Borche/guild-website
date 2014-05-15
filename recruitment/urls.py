
from django.conf.urls import patterns, url

from recruitment import views

urlpatterns = patterns('',
    url(r'^$', views.status, name='status'),
	url(r'^applications/', views.applications, name='applications'),
	url(r'^apply/', views.apply, name='apply'),
	url(r'^process_application/', views.process_application, name='process_application'),
)