from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import redirect
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
    return render(request, 'teachers.html', {'student_tickets': student_tickets})
def manage(request,ticket_id):
    student_ticket = Tickets.objects.get(id=ticket_id)
    if request.method == 'POST':
        form = ManageForm(request.POST)
        if form.is_valid():
            pt_name = form.cleaned_data['pt']
            #pt_name = request.POST.get('complete')
            Tickets.objects.filter(id=ticket_id).update(peer=pt_name)
            Tickets.objects.filter(id=ticket_id).update(completed=True)
            return redirect('/teachers/')
    form = ManageForm()
    return render(request, 'detail.html', {'student_ticket': student_ticket,'form': form})