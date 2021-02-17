from django.shortcuts import render
from django.http import HttpResponse
from Aplicaciones.app_1.models import DePrueba

# Create your views here.
def hola_mundo(request):
	a = DePrueba.objects.all()[0].nombre
	return HttpResponse("Hola " + a)