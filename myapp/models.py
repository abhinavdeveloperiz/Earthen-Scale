from django.db import models

# Create your models here.
class Property_model(models.Model):
    name=models.CharField(max_length=100)
    client_name=models.CharField(max_length=100,null=True,blank=True)
    location=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    area=models.CharField(max_length=100)
    status_choices=(
        ("ON GOING","ON GOING"),
        ("COMPLETED","COMPLETED"),
    )
    status=models.CharField(choices=status_choices,max_length=100)
    image1=models.ImageField(upload_to='images/')
    image2=models.ImageField(upload_to='images/',null=True,blank=True)
    image3=models.ImageField(upload_to='images/',null=True,blank=True)
    image4=models.ImageField(upload_to='images/',null=True,blank=True)
    image5=models.ImageField(upload_to='images/',null=True,blank=True)
    image6=models.ImageField(upload_to='images/',null=True,blank=True)
    image7=models.ImageField(upload_to='images/',null=True,blank=True)
    
    def __str__(self):
        return f"{self.name} / {self.client_name}"


class Hiring(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    postition_choice=(
        ('developer','developer'),
        ('designer','designer'),
        ('manager','manager'),
        ('analyst','analyst')
    )
    position=models.CharField(max_length=100,choices=postition_choice)
    resume=models.FileField(upload_to='resumes/')
    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    message=models.TextField()
    def __str__(self):
        return self.name