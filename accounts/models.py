from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ClientPicture = models.ImageField()
    IsBlock = models.BooleanField(default=False)
    PhoneNumber = models.CharField(max_length=11)
    email = models.CharField(max_length=255)