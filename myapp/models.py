from django.db import models

# Create your models here.

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