from django.core.mail import send_mail
from django.conf import settings
import random
from .models import User


def otp_verification(email):
    subject = 'abc'
    otp = random.randint(1000,9999)
    email_from = settings.EMAIL_HOST
    message = f'your otp is {otp}'
    send_mail(subject,otp,message, email_from ,'sagarsingh94444@gmail.com', ["paramjeet6779@gmail.com"],fail_silently=False)
    user_obj = User.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()
