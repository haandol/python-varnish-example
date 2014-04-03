from django.conf.urls import *

urlpatterns = patterns('main.views',
    url(r'^$', 'index_view'),
    url(r'^static_section/?$', 'static_view'),
    url(r'^dynamic_section/?$', 'dynamic_view'),
)
