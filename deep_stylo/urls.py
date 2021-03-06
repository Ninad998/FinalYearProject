# coding=utf-8
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.pred_list, name='pred_list'),
    url(r'^query/new/$', views.query_new, name='query_new'),
    url(r'^query/(?P<pk>\d+)/remove/$', views.query_remove, name='query_remove'),
]
