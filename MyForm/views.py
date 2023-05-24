from django.shortcuts import render
from .models import MyForm
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        email_from = settings.EMAIL_HOST_USER # see line 97 of settings.py file
        recipient_list = [email, ] #only a list is accepted as a parameter
        message = 'Hey ' + name + '! Thank you for submitting your form. Here is a copy of responses that you submitted\n\n Name: ' + name + "\n Phone No: " + phone + "\n Email ID: " + email + "\n\nThank You"
        send_mail( 'Copy of Responses', message , email_from, recipient_list, fail_silently=False)
    return render(request, 'index.html')