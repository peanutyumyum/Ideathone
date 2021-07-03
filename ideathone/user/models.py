from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    e_mail = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=100)
    