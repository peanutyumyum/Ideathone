from django.urls import path
from .views import *

app_name = 'user'

urlpatterns=[
    path('', search, name = 'search'),
    path('recommend_items', recommend_items, name = 'recommend_items'),
]