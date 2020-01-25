from django.shortcuts import render
from django.http import HttpResponse
from .models import Tickets

# Create your views here.
def index(request):
    students = Tickets.objects.all()
    output = ', '.join([t.name for t in students])
    return HttpResponse(output)