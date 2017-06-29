# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import PollTable
import json
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

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
        dict={"constitueny":const,"constituency-code":const_code,"Leading-Candidate":lead_cand,"Leading-Party":lead_party,"Trailing-Candidate":trial_cand,"Trailing_Party":trail_part,"Margin":marg,"Status":status,"State":state,"State-Code":state_c}
        list.append(dict)
    return HttpResponse(json.dumps(list), content_type="application/json")

# Create your views here.
