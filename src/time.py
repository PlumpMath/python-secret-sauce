# -*- coding: utf-8 -*-
import datetime
import time

def fmtNow():
    return datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')

def fmtNowISO():
    return datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')

def epocTime(long_time):
    return datetime.datetime.fromtimestamp(long_time)

def epochTimeStr(long_time):
    return datetime.datetime.fromtimestamp(long_time).strftime('%Y-%m-%dT%H:%M:%S')

def parseStrTimeToEpoch(strTime, pattern):
    return time.mktime(time.strptime(strTime, pattern))

