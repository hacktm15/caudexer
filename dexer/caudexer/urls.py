from django.conf.urls import url
from caudexer import views

urlpatterns = [
    url(r'^api/search/$', views.search),
]
