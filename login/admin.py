from django.contrib import admin
from .models import *
# Register your models here.


class loginAdmin(admin.ModelAdmin):
    admin.site.register(login)

#class loginData(admin.ModelAdmin):
#   list_display=["name","number","otp"]
#admin.site.register(login,loginData)
