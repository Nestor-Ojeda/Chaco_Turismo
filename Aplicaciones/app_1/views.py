from django.shortcuts import render
from django.http import HttpResponse
from Aplicaciones.app_1.models import *

# Create your views here.
def hola_mundo(request):
	a = DePrueba.objects.all()[0].nombre
	return HttpResponse("Hola " + a)

def paisLista(request):
    pais = Paises.objects.all()
    return render(request, 'gestionPaises.html', {'pais': pais})


def provinciaLista(request):
	provincia = Provincia.objects.all()
	return render(request, 'gestionProvincias.html', {'provincia': provincia})

def ciudadLista(request):  
	ciudad = Ciudad.objects.all()
	return render(request, 'gestionCiudades.html', {'ciudad': ciudad})