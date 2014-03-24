from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'guild.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^forum/', include('forum.urls', namespace="forum")),
    url(r'^roster/', include('roster.urls', namespace="roster")),
    url(r'^admin/', include(admin.site.urls)),
)
