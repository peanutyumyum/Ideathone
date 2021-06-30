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
    search_forms = SearchForm()
    search_word = request.GET.get('search_word')
    context = {
        'recommend_forms' : recommend_forms,
        'search_forms' : search_forms,
        'search_word' : search_word,
    }
    return render(request, 'recommend.html', context)