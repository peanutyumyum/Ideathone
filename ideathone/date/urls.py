from django.urls import path
from .views import *

app_name = 'date'

urlpatterns=[
    path('calendar/', calendar, name = 'calendar'),
]