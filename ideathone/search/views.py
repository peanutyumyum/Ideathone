from django.shortcuts import render

from .models import Item
from django.db.models import Q

# Create your views here.

def search(request):
    items = Item.objects.all()
    search_word = request.GET.get('q')
    
    