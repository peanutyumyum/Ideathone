from django.shortcuts import render

from .models import Item
from django.db.models import Q

from .forms import *

# Create your views here.

def search(request):
    items = Item.objects.all()
    search_word = request.GET.get('search_word')
    if search_word:
        search_items = items.filter(Q(name__icontains = search_word))
        if search_items:   
            context = {
                'search_word' : search_word,
                'search_items' : search_items
            }
            return render(request, 'search.html', context)
        else:
            context = {
                'search_word' : search_word,
            }
            return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')
    
def recommend_items(request):
    items = Item.objects.all()
    recommend_forms = RecommendForm()
    
    place = request.GET.get('place')
    place_size = request.GET.get('place_size')
    style = request.GET.get('style')
    color = request.GET.get('color')
    size = request.GET.get('size')

    if place and place_size and style and color and size:
        search_items = items.filter(Q(place__icontains = place) | Q(place_size__icontains = place_size) | Q(style__icontains = style) | Q(color__icontains = color) | Q(size__icontains = size))
        context = {
            'recommend_forms' : recommend_forms,
            'search_items' : search_items,
        }
        return render(request, 'recommend.html', context)
    else:
        context = {
        'recommend_forms' : recommend_forms,
        }
        return render(request, 'recommend.html', context)
    