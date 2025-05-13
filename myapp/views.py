from django.shortcuts import render
from .models import Hiring, Contact,Property_model
from myapp.forms import Hiring_Form, Contact_form
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.contrib import messages
# Create your views here.


def index(request):
    if request.method=="POST":
        form=Contact_form(request.POST)
        if form.is_valid():
            contact = form.save()
            messages.success(request,"successfully submitted the form")
            subject = "New Enquiry"

            html_content = f"""
            <div style="max-width: 500px; margin: auto; background-color: #000000; color: #ffffff; font-family: 'Arial', sans-serif; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.5);">
                <div style="background-color: #00264d; padding: 20px; text-align: center;">
                    <h2 style="margin: 0; font-size: 22px;">New Enquiry Details</h2>
                </div>
                <div style="padding: 20px;">
                    <p style="margin: 10px 0;"><strong>Name:</strong> {contact.name}</p>
                    <p style="margin: 10px 0;"><strong>Email:</strong> <b style="color: #1e90ff;">{contact.email}</b></p>
                    <p style="margin: 10px 0;"><strong>Phone:</strong> <a href="tel:{contact.phone}" style="color: #1e90ff; text-decoration: none;">{contact.phone}</a></p>
                    <p style="margin: 10px 0;"><strong>Message:</strong></p>
                    <p style="margin: 10px 0; padding-left: 10px; border-left: 3px solid #1e90ff;">{contact.message}</p>
                </div>
                <div style="background-color: #111111; padding: 10px; text-align: center; font-size: 12px; color: #888;">
                    <p style="margin: 0;">You received this message via your website's contact form.</p>
                </div>
            </div>
            """

            plain_text = strip_tags(html_content)  # Fallback text version for plain-text email clients

            email = EmailMultiAlternatives(
                subject=subject,
                body=plain_text,
                from_email=settings.EMAIL_HOST_USER,
                to=[settings.CONTACT_EMAIL]
            )
            email.attach_alternative(html_content, "text/html")
            email.send()

    else:
        form=Contact_form()
    return render(request, 'index.html',{'form':form})



def who(request):
    return render(request, 'who_we_are.html')

def projects(request):
    property=Property_model.objects.all()
    return render(request, 'projects.html',{'property':property})

def project_details(request,id):
    property_details=Property_model.objects.get(id=id)
    return render(request, 'projects_details.html',{'details':property_details})

def what(request):
    return render(request, 'what_we_offer.html')

def career(request):
    
    return render(request, 'careers.html')

def contact(request):
    if request.method=="POST":
        form=Contact_form(request.POST)
        if form.is_valid():
            contact = form.save()
            messages.success(request,"successfully submitted the form")

            subject = "New Enquiry"

            html_content = f"""
            <div style="max-width: 500px; margin: auto; background-color: #000000; color: #ffffff; font-family: 'Arial', sans-serif; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.5);">
                <div style="background-color: #00264d; padding: 20px; text-align: center;">
                    <h2 style="margin: 0; font-size: 22px;">New Enquiry Details</h2>
                </div>
                <div style="padding: 20px;">
                    <p style="margin: 10px 0;"><strong>Name:</strong> {contact.name}</p>
                    <p style="margin: 10px 0;"><strong>Email:</strong> <b style="color: #1e90ff;">{contact.email}</b></p>
                    <p style="margin: 10px 0;"><strong>Phone:</strong> <a href="tel:{contact.phone}" style="color: #1e90ff; text-decoration: none;">{contact.phone}</a></p>
                    <p style="margin: 10px 0;"><strong>Message:</strong></p>
                    <p style="margin: 10px 0; padding-left: 10px; border-left: 3px solid #1e90ff;">{contact.message}</p>
                </div>
                <div style="background-color: #111111; padding: 10px; text-align: center; font-size: 12px; color: #888;">
                    <p style="margin: 0;">You received this message via your website's contact form.</p>
                </div>
            </div>
            """

            plain_text = strip_tags(html_content)  # Fallback text version for plain-text email clients

            email = EmailMultiAlternatives(
                subject=subject,
                body=plain_text,
                from_email=settings.EMAIL_HOST_USER,
                to=[settings.CONTACT_EMAIL]
            )
            email.attach_alternative(html_content, "text/html")
            email.send()

    else:
        form=Contact_form()
    return render(request, 'contact_us.html',{"form":form})