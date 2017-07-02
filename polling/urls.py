from django.conf.urls import url
from  . import views

urlpatterns=[
    url(r'^state$',views.get_value,name="get_value"),
    url(r'^location$',views.get_location,name="get_location"),
    url(r'^html$',views.get_html,name="gethtml"),
    url(r'^$',views.index,name="index"),
    url(r'^bjp$',views.get_bjp,name="bjp"),
    url(r'^tdp$',views.get_tdp,name="tdp"),
    url(r'^cng$',views.get_cong,name="cng"),
]