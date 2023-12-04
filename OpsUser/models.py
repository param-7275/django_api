from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from .validate import validate_file_extension
# Create your models here.

class OpsUser(models.Model):
    upload_file = models.FileField(upload_to='files',validators= [validate_file_extension])
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)