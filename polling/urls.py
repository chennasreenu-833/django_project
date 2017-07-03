from django.conf.urls import url
from  . import views

urlpatterns=[
    url(r'^state$',views.get_value,name="get_value"),
    url(r'^location$',views.get_location,name="get_location"),
    url(r'^html$',views.get_html,name="gethtml"),
    url(r'^login$',views.get_login,name="getlogin"),
    url(r'^add_data$',views.addData,name="addData"),
    url(r'^save$',views.saveData,name="saveData"),
    url(r'^option_entry',views.get_OptionForm,name="optionEntryForm"),
    url(r'^$',views.index,name="index"),
    url(r'^leadparty$',views.get_leadparty,name="leadparty"),
    url(r'^trailparty$', views.get_trialparty, name="trailparty"),
    url(r'^get_list_leadparty$',views.get_list_leadparty,name="getlistleadparty"),
    url(r'^get_list_trailparty$',views.get_list_trailparty,name="getlisttrailparty"),
    url(r'^get_list_state$', views.get_list_state, name="getliststate"),
    url(r'^bjp$',views.get_bjp,name="bjp"),
    url(r'^tdp$',views.get_tdp,name="tdp"),
    url(r'^cng$',views.get_cong,name="cng"),
]