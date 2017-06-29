# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import PollTable
from django.shortcuts import render
from django.http import HttpResponse

def get_value(request):
    key=request.GET.get('id','')
    record=PollTable.objects.get(id=key)
    list=[]
    list.append(record.constituency)
    list.append(record.constituency_code)
    list.append(record.leading_candidate)
    list.append(record.leading_party)
    list.append(record.trailing_candidate)
    list.append(record.trailing_party)

    return HttpResponse(list)

# Create your views here.
