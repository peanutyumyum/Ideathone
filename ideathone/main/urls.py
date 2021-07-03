from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'main'

urlpatterns=[
    path('', main, name = 'main')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)