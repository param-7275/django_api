from django.contrib import admin
from .models import*
# Register your models here.

# Register your models here.

class OpsUserAdmin(admin.ModelAdmin):
    list_display = ['id','upload_file','uploaded_by']
admin.site.register(OpsUser,OpsUserAdmin)