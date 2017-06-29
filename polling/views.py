# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import PollTable
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def get_value(request):
    key=request.GET.get('id','')
    record=PollTable.objects.get(id=key)
    const=record.constituency
    const_code=record.constituency_code
    lead_cand=record.leading_candidate
    lead_party=record.leading_party
    trial_cand=record.trailing_candidate
    trail_part=record.trailing_party
    marg=record.margin
    status=record.status
    state=record.state
    state_c=record.state_code
    dict={"constitueny":const,"constituency-code":const_code,"Leading-Candidate":lead_cand,"Leading-Party":lead_party,"Trailing-Candidate":trial_cand,"Trailing_Party":trail_part,"Margin":marg,"Status":status,"State":state,"State-Code":state_c}

    return JsonResponse(dict)

# Create your views here.
