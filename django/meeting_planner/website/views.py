from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from meetings.models import Meeting
# Create your views here.


def welcome(req):
    return render(req, "website/welcome.html", {"num_meetings": Meeting.objects.all()})


def date(req):
    return HttpResponse(f'This page was served at {str(datetime.now())}')

def about(req):
    return HttpResponse('My name is Noah Loomis and I\'m crazy about Django!')