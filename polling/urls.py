from django.conf.urls import url
from  . import views

urlpatterns=[
    url(r'^state$',views.get_value,name="get_value"),
    url(r'^location$',views.get_location,name="get_location"),
    url(r'^$',views.index,name="index"),
]