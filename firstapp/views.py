from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def wish(request):
    message = '<h1>Wish you all success</h1>'
    return HttpResponse(message)

def tellTime(request):
    time = datetime.datetime.now()
    message = '<h1>Hi the time is : '+str(time)+'</h1>'
    return HttpResponse(message)

