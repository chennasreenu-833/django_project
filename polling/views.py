# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import PollTable,Location,LoginDetails
from django.db.models import Count

import json
from django.http import HttpResponse
def index(request):
    return HttpResponse("""<html>
    <head><title>polling api</title></head>
    <h1><center>Welcome To Polling API</center></h1>
    </html>""")
def saveData(request):
    try:
        constituency=request.POST.get('constituency','')
        constituency_code=request.POST.get('constituency_code','')
        leading_party=request.POST.get('leading_party','')
        leading_candidate=request.POST.get('leading_candidate','')
        trailing_candidate=request.POST.get('trailing_candidate','')
        trailing_party=request.POST.get('trailing_party','')
        margin=int(request.POST.get('margin',''))
        state=request.POST.get('state','')
        state_code=request.POST.get('state_code','')
        latitude=request.POST.get('latitude','')
        longitude=request.POST.get('longitude','')
        status="Results Declared"
        polling_rec=PollTable(constituency=constituency,constituency_code=constituency_code,leading_candidate=leading_candidate,leading_party=leading_party,trailing_candidate=trailing_candidate,trailing_party=trailing_party,margin=margin,status=status,state=state,state_code=state_code)
        location_rec=Location(constituency=constituency,latitude=latitude,longitude=longitude)
        polling_rec.save()
        location_rec.save()
        return HttpResponse("SUCCESS")
    except:
        return HttpResponse("FAILED")

def addData(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    record=LoginDetails.objects.filter(username=username)
    if(record[0].password==password):
        return HttpResponse("TRUE")
    else:
        return HttpResponse("FALSE")
def get_value(request):
    key=request.GET.get('state','')
    record=PollTable.objects.filter(state=key)
    list=[]
    for each_rec in record:
        const=each_rec.constituency
        const_code=each_rec.constituency_code
        lead_cand=each_rec.leading_candidate
        lead_party=each_rec.leading_party
        trial_cand=each_rec.trailing_candidate
        trail_part=each_rec.trailing_party
        marg=each_rec.margin
        status=each_rec.status
        state=each_rec.state
        state_c=each_rec.state_code
        #print const,const_code,lead_party,lead_cand,trail_part,trial_cand,marg,status,state

        try:
            location_rec = Location.objects.get(constituency=const)
            lat = float(location_rec.latitude)
            long = float(location_rec.longitude)
        except:
            location_rec = Location.objects.filter(constituency=const)
            lat = float(location_rec[0].latitude)
            long = float(location_rec[0].longitude)
       # print lat,long
        dict={"constituency":const,"constituency_code":const_code,"Leading_Candidate":lead_cand,"Leading_Party":lead_party,"Trailing_Candidate":trial_cand,"Trailing_Party":trail_part,"Margin":marg,"Status":status,"State":state,"State_Code":state_c,"Latitude":lat,"Longitude":long}

        list.append(dict)
    return HttpResponse(json.dumps(list), content_type="application/json")

def get_leadparty(request):
    key=request.GET.get('leadparty','');
    records=PollTable.objects.filter(leading_party=key)
    list=[]
    for each_rec in records:
        consti=each_rec.constituency
        consti_code=each_rec.constituency_code
        lead_cand=each_rec.leading_candidate
        margin=each_rec.margin
        try:
            location_rec = Location.objects.get(constituency=consti)
            lat = float(location_rec.latitude)
            long = float(location_rec.longitude)
        except:
            location_rec = Location.objects.filter(constituency=consti)
            lat = float(location_rec[0].latitude)
            long = float(location_rec[0].longitude)
        dict={"constituency":consti,"constituency_code":consti_code,"Leading_Candidate":lead_cand,"Margin":margin,"Latitude":lat,"Longitude":long}
        list.append(dict)
    return HttpResponse(json.dumps(list),content_type="application/json")

def get_trialparty(request):
    key=request.GET.get('trailparty','');
    records=PollTable.objects.filter(trailing_party=key)
    list=[]
    for each_rec in records:
        consti=each_rec.constituency
        consti_code=each_rec.constituency_code
        trail_cand=each_rec.trailing_candidate
        margin=each_rec.margin
        try:
            location_rec = Location.objects.get(constituency=consti)
            lat = float(location_rec.latitude)
            long = float(location_rec.longitude)
        except:
            location_rec = Location.objects.filter(constituency=consti)
            lat = float(location_rec[0].latitude)
            long = float(location_rec[0].longitude)
        dict={"constituency":consti,"constituency_code":consti_code,"Trailing_Candidate":trail_cand,"Margin":margin,"Latitude":lat,"Longitude":long}
        list.append(dict)
    return HttpResponse(json.dumps(list),content_type="application/json")
def get_pie(request):
    records=list(PollTable.objects.values('leading_party').annotate(dcount=Count('leading_party')))
    return HttpResponse(json.dumps(records),content_type="application/json")
def open_piechart(request):
    foo = open("pie_chart.html", "r+")
    file_date = foo.read()
    foo.close()
    return HttpResponse(file_date, content_type="text/html")

def get_location(request):
    key=request.GET.get('constituency','')
    try:
        record=Location.objects.get(constituency=key)
        lat = float(record.latitude)
        long = float(record.longitude)
    except:
        record = Location.objects.filter(constituency=key)
        lat = float(record[0].latitude)
        long = float(record[0].longitude)
    list=[]
    dict={"constituency":key,"latitude":lat,"longitude":long}
    list.append(dict)
    return HttpResponse(json.dumps(list),content_type="application/json")

def get_list_state(request):
    records=PollTable.objects.values('state').distinct()
    list=[]
    for each_rec in records:
        list.append(each_rec);
    return HttpResponse(json.dumps(list),content_type="application/json")

def get_list_leadparty(request):
    records=PollTable.objects.values('leading_party').distinct()
    list=[]
    for each_rec in records:
        list.append(each_rec);
    return HttpResponse(json.dumps(list),content_type="application/json")
def get_list_trailparty(request):
    records=PollTable.objects.values('trailing_party').distinct()
    list=[]
    for each_rec in records:
        list.append(each_rec);
    return HttpResponse(json.dumps(list),content_type="application/json")
def get_html(request):
    foo=open("maps.html","r+")
    file_date=foo.read()
    foo.close()
    return HttpResponse(file_date,content_type="text/html")
def get_login(request):
    foo=open("login.html","r+")
    file_date=foo.read()
    foo.close()
    return HttpResponse(file_date,content_type="text/html")
def get_OptionForm(request):
    foo=open("add_data.html","r+")
    file_data=foo.read()
    foo.close()
    return HttpResponse(file_data,content_type="text/html")
def get_bjp(request):
    foo=open("bjp.png","rb+")
    file_data=foo.read()
    foo.close()
    return HttpResponse(file_data,content_type="image/png")
def get_tdp(request):
    foo=open("tdp.png","rb+")
    file_data=foo.read()
    foo.close()
    return HttpResponse(file_data,content_type="image/png")
def get_cong(request):
    foo=open("cong.png","rb+")
    file_data=foo.read()
    foo.close()
    return HttpResponse(file_data,content_type="image/png")


# Create your views here.
