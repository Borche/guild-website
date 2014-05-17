
from django.conf.urls import patterns, url

from account import views

urlpatterns = patterns('',
    url(r'^$', views.registration_page, name='registration_page'),
	url(r'^register/', views.register, name='register'),
)