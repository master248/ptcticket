from django import forms
from .models import Tickets

class ContactForm(forms.Form):
    name = forms.CharField()
    course = forms.ChoiceField(choices=[('121', '121'), ('other', 'Other')])


class TicketsForm(forms.ModelForm):

    class Meta:
        model = Tickets
        fields = ('name','course')
class ManageForm(forms.Form):
    pt = forms.CharField()
    
