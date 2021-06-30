from django.urls import path
from .views import *

app_name = 'user'

urlpatterns=[
    path('', main, name = 'main'),
    path('login/', login_view, name = "login"),
    path('logout/', logout_view, name = "logout"),
    path('signup/', signup_view, name = "signup" ),
    path('create_page/', create_page, name='create_page'),
    path('create/', create, name='create'),
]