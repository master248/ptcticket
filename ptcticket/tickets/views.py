from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Tickets

# Create your views here.
def index(request):
    student_tickets = Tickets.objects.all()
    template = loader.get_template('students/index.html')
    #output = ', '.join([t.name for t in students])
    context = {'student_tickets': student_tickets}
    return render(request, 'students/index.html', context)
# def index(request):
#      return render(request, 'students/index.html')
#return HttpResponse(output)