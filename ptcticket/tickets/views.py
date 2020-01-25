from django.shortcuts import render
from django.http import HttpResponse
from .models import Tickets

# Create your views here.
def index(request):
     return render(request, 'students/index.html')
