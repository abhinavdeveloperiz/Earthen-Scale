from django.shortcuts import render
from .models import Hiring, Contact
from myapp.forms import Hiring_Form, Contact_form
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def index(request):
    if request.method=='post':
        form=Hiring_Form(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=Hiring_Form()
    return render(request, 'index.html',{'form':form})

def who(request):
    return render(request, 'who_we_are.html')

def projects(request):
    return render(request, 'projects.html')

def project_details(request):
    return render(request, 'projects_details.html')

def what(request):
    return render(request, 'what_we_offer.html')

def career(request):
    return render(request, 'careers.html')

def contact(request):
    if request.method=='post':
        form=Contact_form(request.POST)
        if form.is_valid():
            form.save()
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            phone=form.cleaned_data['phone']
            message=form.cleaned_data['message']
            subject='Contact Us Form'
            message=f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}'
            send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
    else:
        form=Contact_form()
    context={'form':form}
    return render(request, 'contact_us.html',context)