from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    ClientPicture = models.ImageField()
    IsBlock = models.BooleanField(default=False)
    PhoneNumber = models.CharField()
    email = models.EmailField(max_length=255, unique=True)