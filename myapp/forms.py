from django import forms
from .models import Hiring, Contact


class Hiring_Form(forms.ModelForm):
    class Meta:
        model=Hiring
        fields = ['name', 'email', 'phone', 'position','resume']
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your full name"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'position': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select Position'}),
            'resume':forms.ClearableFileInput(attrs={"class":"form-control"}),
        }


class Contact_form(forms.ModelForm):
    class Meta:
        model=Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Describe your request'}),
        }