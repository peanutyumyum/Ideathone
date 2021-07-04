from django.shortcuts import render

from .models import Garden, Item
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
                'items' : search_items
            }
            return render(request, 'main.html', context)
        else:
            no_search_data = items.filter(name = 'no_data')
            context = {
                'search_word' : search_word,
                'items' : no_search_data
            }
            return render(request, 'main.html', context)
    else:
        context = {
                'search_word' : search_word,
                'items' : items
            }
        return render(request, 'main.html', context)
    
def recommend_items(request):
    gardens = Garden.objects.all()
    recommend_forms = RecommendForm()
    
    place = request.GET.get('place')
    place_size = request.GET.get('place_size')
    style = request.GET.get('style')
    color = request.GET.get('color')
    size = request.GET.get('size')

    if place and place_size and style and color and size:
        search_gardens = gardens.filter(Q(place__icontains = place) | Q(place_size__icontains = place_size) | Q(style__icontains = style) | Q(color__icontains = color) | Q(size__icontains = size))
        recommend_garden = search_gardens[0] ## 테스트용으로 첫 번째 DB 하나만 가져옴(추천 알고리즘은 나중에 더 연구해봅시다!)
        print(recommend_garden)
        context = {
            'recommend_forms' : recommend_forms,
            'recommend_garden' : recommend_garden,
        }
        return render(request, 'main.html', context)
    else:
        context = {
        'recommend_forms' : recommend_forms,
        }
        return render(request, 'main.html', context)

def detail(request, id):
    item = Item.objects.get(pk=id)
    context = {
        'item' : item,
    }
    return render(request, 'ddetail.html', context)