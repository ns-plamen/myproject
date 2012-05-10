from django.template import RequestContext, loader, Context, Template
from django.template.loader import get_template
#from django.templatetags import Staticfiles
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponseRedirect
from mylens import listdir, fileprint
from mycal import mycalendar
import datetime
import calendar
import os
from calendar import HTMLCalendar
from calendar import TextCalendar
from calendar import monthcalendar
from datetime import date, timedelta, time

def empty(request):
    #print "debug"
    return HttpResponseRedirect ('/index/')

def index(request):
    
    return render_to_response ('task_1/index.html', {} )

def time(request):
    select_day = request.GET.get('mdate', '')
    
    cal_result = mycalendar(select_day)
    return render_to_response ('task_1/time.html', cal_result)

def work(request):
    path = request.GET.get('way', '')
    result = listdir(path)
    #proverka za error v lisdir(path)
    if result == 'error':
        result = 'WRONG PATH!<br><a href="http://127.0.0.1:8000/index/">BACK</a>'
        return HttpResponse(str(result))
    #print type (result)
    return render_to_response ('task_1/result.html', result )
    



