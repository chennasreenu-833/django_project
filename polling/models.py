# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Results(models.Model):
    constituency=models.CharField(max_length=200)
    constituency_code=models.IntegerField()
    leading_candidate=models.CharField(max_length=200)
    leading_party=models.CharField(max_length=200)
    trailing_candidate=models.CharField(max_length=200)
    trailing_party=models.CharField(max_length=200)
    margin=models.IntegerField()
    status=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    state_code=models.CharField(max_length=100)
class PollTable(models.Model):
    constituency = models.CharField(max_length=200)
    constituency_code = models.IntegerField()
    leading_candidate = models.CharField(max_length=200)
    leading_party = models.CharField(max_length=200)
    trailing_candidate = models.CharField(max_length=200)
    trailing_party = models.CharField(max_length=200)
    margin = models.IntegerField()
    status = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    state_code = models.CharField(max_length=100)
class Location(models.Model):
    constituency=models.CharField(max_length=200)
    latitude=models.DecimalField(max_digits=30, decimal_places=15)
    longitude=models.DecimalField(max_digits=30, decimal_places=15)
class LoginDetails(models.Model):
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=25)
# Create your models here.
