from django import forms

class ContactForm(forms.Form):
    first_Name = forms.CharField()
    class_Name = forms.ChoiceField(choices=[('121', '121'), ('other', 'Other')])
    question = forms.CharField(widget=forms.Textarea)
    