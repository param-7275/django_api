from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.
class ClientSignup(models.Model):
    # username = User
    email = models.EmailField(max_length=254,unique=True)
    otp = models.CharField(max_length=50,null=True,blank=True)
    otp_verified = models.BooleanField(max_length=4,default=False)