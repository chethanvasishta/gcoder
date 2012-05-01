from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gcoder.views.home', name='home'),
    # url(r'^gcoder/', include('gcoder.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'coderapp.views.index'),
    url(r'^coder/challenges', 'coderapp.views.challenges'),
    url(r'^coder/challenge/(?P<challenge_id>\d+)/$', 'coderapp.views.challenge'),
    #url(r'^coder/', include(coderapp.urls)),
)
