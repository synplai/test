from django.urls import path
from teste.views import home

urlpatterns = [
    path('', home), #home
]