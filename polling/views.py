# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import PollTable,Location
import json
from django.http import HttpResponse
def index(request):
    return HttpResponse("""<html>
    <head><title>polling api</title></head>
    <h1><center>Welcome To Polling API</center></h1>
    </html>""")
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
        dict={"constituency":const,"constituency-code":const_code,"Leading-Candidate":lead_cand,"Leading-Party":lead_party,"Trailing-Candidate":trial_cand,"Trailing_Party":trail_part,"Margin":marg,"Status":status,"State":state,"State-Code":state_c,"Latitude":lat,"Longitude":long}

        list.append(dict)
    return HttpResponse(json.dumps(list), content_type="application/json")
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
def get_html(request):
    foo=open("maps.html","r+")
    file_date=foo.read()
    foo.close()
    return HttpResponse(file_date,content_type="text/html")




# Create your views here.
