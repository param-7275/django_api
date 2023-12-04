from django.contrib import admin
from .models import*
# Register your models here.

# class ClientUserAdmin(admin.ModelAdmin):
#     list_display = ['id','username','email']
admin.site.register(ClientSignup)