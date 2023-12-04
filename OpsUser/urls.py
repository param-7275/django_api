from django.urls import path
from .views import*



urlpatterns = [
   path('uploadfile/', OpsUploadFiles.as_view(), name="uploadfile"),
   path('opssignup/',  OpsSignUp.as_view(), name="opssignup"),
   path('opslogin/', OpsLogin.as_view(), name="opslogin"),   
]