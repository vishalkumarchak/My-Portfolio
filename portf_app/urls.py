from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('techstack/', views.techstack, name='techstack'),
    path('contact/', views.contact, name='contact'),
    path('send-email/', views.send_email, name='send_email'),
]
