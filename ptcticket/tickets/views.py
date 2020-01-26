from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import ContactForm, TicketsForm



def tickets_detail(request):

     if request.method == 'POST':
          form = TicketsForm(request.POST)
          if form.is_valid():
               form.save()
               return render(request, 'succ.html')

     form = TicketsForm()
     return render(request, 'students.html', {'form': form})
