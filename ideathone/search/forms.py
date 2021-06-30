from django import forms
from django.db.models import fields
from django.db.models.base import Model

CHOICE_LIST = [
    ('1평', '1평'),
    ('2평', '2평'),
]
# (value, text) format

class SearchForm(forms.Form):
    search_word = forms.CharField(widget=forms.TextInput(attrs={'type' : 'search', 'placeholder' : '검색어를 입력하세요', 'value' : '{{search_word}}'}))

class RecommendForm(forms.Form):
    size = forms.ChoiceField(choices = CHOICE_LIST) # it makes select tag
