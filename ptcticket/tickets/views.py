from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import ContactForm
from .models import Tickets

def contact(request):
     form = ContactForm()
     return render(request, 'students.html', {'form': form})
def manage(request):
    student_tickets = Tickets.objects.filter(completed=False)
    return render(request, 'teachers.html', {'student_tickets': student_tickets})
