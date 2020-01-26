from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import ContactForm

def contact(request):
     form = ContactForm()
     return render(request, 'students.html', {'form': form})
