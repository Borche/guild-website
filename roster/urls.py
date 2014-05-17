'''
Created on 28 jan 2014

@author: Andreas
'''

from django.conf.urls import patterns, url

from roster import views

urlpatterns = patterns('',
    url(r'^(?P<attr>\w+)/(?P<ord>\w+)/$', views.roster, name='roster'),
)