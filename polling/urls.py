from django.conf.urls import url
from  . import views

urlpatterns=[
    url(r'^$',views.get_value,name="get_value"),
]