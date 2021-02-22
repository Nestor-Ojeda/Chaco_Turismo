from django.urls import path
from . import views


urlpatterns = [
    path('pais', views.paisLista, name='paisLista'),
    path('provincia', views.provinciaLista, name='provinciaLista'),
    path('ciudad', views.ciudadLista, name='ciudadLista'),
]
