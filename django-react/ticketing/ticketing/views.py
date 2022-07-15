from pyexpat import model
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.forms import modelform_factory

from ticketing.models import Ticket

TicketForm = modelform_factory(Ticket, exclude=[])

class Review(models.Model):
    description = models.CharField(max_length=200)
    added_date = models.DateField()
    
    
def index(req):
    description_body = 'Awesome'
    date=''
    try:
        rev = Review(description=description_body, added_date=date)
        rev.save()
    except IntegrityError as e:
        return HttpResponse({'message':'error when inserting record'})
    return HttpResponse({'message': 'record inserted'})
        # return render(req, "home.html")


def index_jinja(req):
    return render(req, "jinjahome.html")


def tickets_raw(req):
    return JsonResponse(list(Ticket.objects.get(pk=1, decode=True)), safe=False)


def submit(req):
    if req.method == "POST":
        print(req)
        form = TicketForm(req)
        uname = req.POST.get("submitter")
        body = req.POST.get("body")
        new_ticket = Ticket(submitter=uname, body=body)
        new_ticket.save()
        return redirect("tickets")
    else:
        form = TicketForm()
    return render(req, "submit.html", {"form": form})


def base(req):
    return render(req, 'base.html')


def tickets(req):
    print(Ticket.objects.all())
    return render(req, "tickets.html", {'all_tickets': Ticket.objects.all()})
