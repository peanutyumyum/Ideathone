from django import forms
from django.db.models import fields
from django.db.models.base import Model
from django.forms import utils

from django.contrib.auth.forms import UserCreationForm

from .models import  CustomUser

class RegistorForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','password1','password2', 'e_mail','phone_number']