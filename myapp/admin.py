from django.contrib import admin
from .models import Property_model,Contact,Hiring
# Register your models here.

admin.site.register(Property_model)
admin.site.register(Contact)
admin.site.register(Hiring)
