from django.urls import path
from . import views


urlpatterns = [
    path('', views.paisLista, name='paisLista'),
]
