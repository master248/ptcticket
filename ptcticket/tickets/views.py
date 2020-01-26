from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import ContactForm

def contact(request):

     if request.method == 'POST':
          form = ContactForm(request.POST)
          if form.is_valid():
               name = form.cleaned_data['name']
               course = form.cleaned_data['class_category']

               print(name)
               print(course)

     form = ContactForm()
     return render(request, 'students.html', {'form': form})
