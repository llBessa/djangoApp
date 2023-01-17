from django.contrib import admin
from .models import Users, Passwords

# Register your models here.
admin.site.register(Users)
admin.site.register(Passwords)