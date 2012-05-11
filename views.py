from django.template import RequestContext, loader, Context, Template
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render_to_response
from apps.asd.horse import listdir
import datetime
import calendar
from calendar import HTMLCalendar
#from calendar import monthdatescalendar
#from datetime import date

def index(request):
    print 'test'
    return render_to_response ('asd/index.html', {} )

def time(request):
    monthCal = HTMLCalendar(calendar.MONDAY)
    now = datetime.date.today()
    date_0 = now.year
    date_1 = now.month
    date_2 = now.day
    my_cal = monthCal.formatmonth (date_0 ,date_1 )
    my_cal = my_cal.replace ('">%r</td><td class="' %date_2, '"<p style="color:#FF0000">%r</p></td><td class="' %date_2)
    return render_to_response ('asd/time.html', {'current_date': now, 'cal': my_cal  })

def work(request):
    path = request.GET.get('way', '')
    result = listdir(path)
    #proverka za error v lisdir(path)
    if result == 'error':
        result = 'WRONG PATH!<br><a href="http://127.0.0.1:8000/index/">BACK</a>'
        return HttpResponse(str(result))
    print result
    return render_to_response ('asd/result.html', result )
    #return HttpResponse(str(result))
#useless comment for new branch :)
