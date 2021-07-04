from django.contrib import admin
from django.urls import path
# 이미지 삽입 방법
from django.conf.urls.static import static
from django.conf import settings
##
from detailApp.views import main
app_name = 'detailApp'

urlpatterns=[
    path('', main, name= "main"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
