from django import forms
from .models import Hiring, Contact

class Hiring_Form(forms.ModelForm):
    class Meta:
        model=Hiring
        fields='__all__'

class Contact_form(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'