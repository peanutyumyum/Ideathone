from django import forms
from django.db.models import fields
from django.db.models.base import Model

PLACE_LIST = [
    ('실내', '실내'),
    ('실외', '실외'),
]

PLACE_SIZE_LIST = [
    ('5평', '5평'),
    ('6평', '6평'),
    ('7평', '7평'),
    ('8평', '8평'),
    ('9평', '9평'),
    ('10평', '10평'),
    ('11평', '11평'),
    ('12평', '12평'),
    ('13평', '13평'),
]

STYLE_LIST = [
    ('산뜻한', '산뜻한'),
    ('푸르른', '푸르른'),
]

COLOR_LIST = [
    ('밝은', '산뜻한'),
    ('어두운', '푸르른'),
    ('초록', '초록'),
]

SIZE_LIST = [
    ('손바닥', '손바닥'),
    ('A4용지', 'A4용지'),
    ('책상', '책상'),
]
# (value, text) format

class RecommendForm(forms.Form):
    place = forms.ChoiceField(choices = PLACE_LIST, widget = forms.TextInput(attrs={'id' : 'place'})) 
    place_size = forms.ChoiceField(choices = PLACE_SIZE_LIST, widget = forms.TextInput(attrs={'id' : 'place_size'}))
    style = forms.ChoiceField(choices = SIZE_LIST, widget = forms.TextInput(attrs={'id' : 'style'}))
    color = forms.ChoiceField(choices = COLOR_LIST, widget = forms.TextInput(attrs={'id' : 'color'}))
    size = forms.ChoiceField(choices = SIZE_LIST, widget = forms.TextInput(attrs={'id' : 'size'}))
    # it makes select tag