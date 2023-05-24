This is an example of a Django Form which sends Copy of Responses as an email to the user.


How To Use:
 1) Provide permission to the Gmail account from which mails have to be sent. 
  
    Steps :
    In your Gmail Account: Manage Account -> How to Sign In -> Turn 2 step verification on -> Go to App Passwords -> Select Device and App -> Generate a 16 digit password
 2) Go to settings.py file of the Django project
 
    Replace the EMAIL_HOST_USER on line 97 with your gmail id and replace EMAIL_HOST_PASSWORD on line 98 with the password generated on step 1
 3) Run the Django Project
  
    pip install any_required_dependencies -> python manage.py makemigrations -> python manage.py migrate -> python manage.py runserver
  
  
Tech Stack:

django.core.mail library
