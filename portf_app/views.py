from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'index.html') 

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def techstack(request):
    return render(request, 'techstack.html')

def contact(request):
    return render(request, 'contact.html')

def send_email(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        subject = f"Portfolio Contact from {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(subject, body, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, 'Oops! Something went wrong. Please try again later.')

    return redirect('contact')

