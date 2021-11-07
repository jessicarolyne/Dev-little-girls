from django.conf.urls import patterns, url
from site_devlittlegirls_app import views

urlpatterns = patterns('',
                       url(r'^', views.index, name='index'),
#                       url(r'^', views.more, name='more'),
                       )
