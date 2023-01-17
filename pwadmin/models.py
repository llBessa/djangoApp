from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=320, null=False)
    password = models.CharField(max_length=30, null=False)
    created_at = models.DateTimeField(null=False)

class Passwords(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    label = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=100, null=False)
