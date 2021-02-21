from django.db import models

# Create your models here.

class DePrueba(models.Model):
		nombre = models.CharField(max_length = 50)

class Paises(models.Model):
		codigo = models.CharField(max_length = 2)
		pais = models.CharField(max_length=100)

class Provincia(models.Model):
	nombre = models.CharField(max_length=100)

class Ciudad(models.Model):
	cod_Postal = models.CharField(max_length=10)
	nom_ciudad = models.CharField(max_length=100)
	zona_turismo = models.CharField(max_length=100)






