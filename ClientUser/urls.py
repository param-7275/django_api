from django.urls import path
from .import views
from .views import*

urlpatterns = [

   path('clientsignup/', ClientSignup.as_view(), name="clientsignup"),
   path('clientlogin/', ClientLogin.as_view(), name="clientlogin"),
   path('showfiles/', ShowFiles.as_view(), name="showfiles"),
   path('otp/', Verify_otp.as_view(), name="otp"),

]