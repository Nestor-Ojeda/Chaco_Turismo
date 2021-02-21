from django.db import models

# Create your models here.

class DePrueba(models.Model):
		nombre = models.CharField(max_length = 50)

class Paises(models.Model):
		codigo = models.CharField(max_length = 2)
		pais = models.CharField(max_length=100)




