from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    class_category = forms.ChoiceField(choices=[('121', '121'), ('other', 'Other')])
class ManageForm(forms.Form):
    pt = forms.CharField()
    