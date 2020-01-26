from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import ContactForm
from .forms import ManageForm
from .forms import TicketsForm
from .models import Tickets

def tickets_detail(request):

    if request.method == 'POST':
        form = TicketsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'succ.html')

    form = TicketsForm()
    return render(request, 'students.html', {'form': form})
def student_list(request):
    student_tickets = Tickets.objects.filter(completed=False)
    return render(request, 'teachers.html', {'student_tickets': student_tickets,'form': form})
def manage(request):
    student_tickets = Tickets.objects.filter(completed=False)
    if request.method == 'POST':
        form = ManageForm(request.POST)
        if form.is_valid():
            Tickets.objects.filter(id=6).update(completed=True)
    form = ManageForm()
    return render(request, 'teachers.html', {'student_tickets': student_tickets,'form': form})