'''
Created on 28 jan 2014

@author: Andreas
'''

from django.conf.urls import patterns, url

from forum import views

urlpatterns = patterns('',
    url(r'^$', views.forums, name='forums'),
    url(r'^(?P<f_id>\d+)/$', views.threads, name='threads'),
    url(r'^thread/(?P<t_id>\d+)/$', views.comments, name='comments'),
    url(r'^thread/(?P<t_id>\d+)/new_comment/$', views.new_comment, name='new_comment'),
)