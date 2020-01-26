from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import ContactForm
from .forms import ManageForm
from .models import Tickets

def tickets_detail(request):

    if request.method == 'POST':
        form = TicketsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'succ.html')

    form = TicketsForm()
    return render(request, 'students.html', {'form': form})
def manage(request):
    if request.method == 'POST':
        form = ManageForm(request.POST)
        student_tickets = Tickets.objects.filter(completed=False)
        if form.is_valid():
            completed = Tickets.objects
    form = ManageForm()
    return render(request, 'teachers.html', {'student_tickets': student_tickets,'form': form})
