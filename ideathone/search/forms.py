from django import forms
from django.db.models import fields
from django.db.models.base import Model

a = '11평', '22평'

class RecommendForm(forms.Form):
    size = forms.ChoiceField(choices = a)