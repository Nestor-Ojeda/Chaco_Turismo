from django.shortcuts import render
from django.http import HttpResponse
from Aplicaciones.app_1.models import DePrueba, Paises

# Create your views here.
def hola_mundo(request):
	a = DePrueba.objects.all()[0].nombre
	return HttpResponse("Hola " + a)
"""
def paisLista(request):
		paisListados = Paises.objects.all()
    	return render(request, "gestionPaises.html", {'paises': paisListados})

"""
def paisLista(request):
    pais = Paises.objects.all()
    return render(request, 'gestionPaises.html', {'pais': pais})


