from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import Tickets

class ContactForm(forms.Form):
    name = forms.CharField(max_length=15)
    course = forms.ChoiceField(choices=[('121', '121'), ('other', 'Other')])


class TicketsForm(forms.ModelForm):

    class Meta:
        model = Tickets
        fields = ('name','course','question')
class ManageForm(forms.Form):
    pt = forms.CharField()