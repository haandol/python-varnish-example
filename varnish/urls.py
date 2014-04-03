#coding: utf-8

from django.conf import settings

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'', include('main.urls')),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
