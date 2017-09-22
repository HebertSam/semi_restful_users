from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^make$', views.new_user),
    url(r'^create$', views.create),
    url(r'^show/(?P<id>\w+)$', views.show),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^update/(?P<id>\d+)$', views.update),

]