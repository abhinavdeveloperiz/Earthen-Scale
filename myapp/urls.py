from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('who-we-are', views.who, name='who-we-are'),
    path('projects', views.projects, name='projects'),
    path('project-details', views.project_details, name='projects-details'),
    path('what-we-offer', views.what, name='what-we-offer'),
    path('careers', views.career, name='careers'),
    path('contact-us', views.contact, name='contact-us'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)