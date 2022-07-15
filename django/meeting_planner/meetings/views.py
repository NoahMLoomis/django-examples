import re
from django.shortcuts import get_object_or_404, redirect, render
from django.forms import modelform_factory

from meetings.models import Meeting, Room

from .forms import MeetingForm


def detail(req, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(req, "meetings/detail.html", {"meeting": meeting})


def allRooms(req):
    return render(req, "meetings/rooms.html", {"all_rooms": Room.objects.all()})


def new(req):
    if req.method == "POST":
        form = MeetingForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(req, "meetings/new.html", {"form": form})
