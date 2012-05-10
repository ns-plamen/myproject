#!/usr/bin/env python
import datetime
import calendar
from calendar import monthcalendar
from datetime import date, timedelta, time


def mycalendar (select_day):
    select_day = str(select_day)
    old_select = None
    if select_day != '':
        last_select = len(select_day)
        if select_day[-1] == ' ':
            last_select = last_select - 1
        old_select = map(int, select_day[0:(last_select)].split(' '))
    now = datetime.date.today()
    cal = calendar.Calendar()
    date_0 = now.year
    date_1 = now.month
    date_2 = now.day
    jq_month = date_1 - 1
    #calculating weekdays in month main_2nd.js don't need this
    monthlist = calendar.monthcalendar(date_0, date_1)
    month_monday = []
    month_tuesday = []
    month_wednesday = []
    month_thursday = []
    month_friday = []
    month_saturday = []
    month_sunday = []
    for week in monthlist:
        if (week[0]) != 0:
            month_monday.append(week[0])
    for week in monthlist:
        if (week[1]) != 0:
            month_tuesday.append(week[1])
    for week in monthlist:
        if (week[2]) != 0:
            month_wednesday.append(week[2])
    for week in monthlist:
        if (week[3]) != 0:
            month_thursday.append(week[3])
    for week in monthlist:
        if (week[4]) != 0:
            month_friday.append(week[4])
    for week in monthlist:
        if (week[5]) != 0:
            month_saturday.append(week[5])
    for week in monthlist:
        if (week[6]) != 0:
            month_sunday.append(week[6])   
    myresult = {'now': (now),
                'monthlist':(monthlist),
                'date_2': (date_2),
                'selection': (select_day),
                'selection_list': (old_select),
                'now_month': (jq_month),
                'now_year': (date_0),
                'monthdays': (monthlist),
                'monthMonday': (month_monday),
                'monthTuesday': (month_tuesday),
                'monthWednesday': (month_wednesday),
                'monthThursday': (month_thursday),
                'monthFriday': (month_friday),
                'monthSaturday': (month_saturday),
                'monthSunday': (month_sunday)
               }
    return myresult
