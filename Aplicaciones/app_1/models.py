from django.db import models

# Create your models here.

class DePrueba(models.Model):
		nombre = models.CharField(max_length = 50)

class Paises(models.Model):
		codigo = models.CharField(max_length = 2)
		pais = models.CharField(max_length=100)

		def __str__(self):
			texto = '{0}-{1}'
			return texto.format(self.codigo, self.pais)

class Provincia(models.Model):
	pais = models.ForeignKey(Paises, on_delete=models.SET_NULL, null=True)
	nombre = models.CharField(max_length=100)

	def __str__(self):
			texto = '{0}-{1}'
			return texto.format(self.pais, self.nombre)

class Ciudad(models.Model):
	provincia = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True)
	cod_Postal = models.CharField(max_length=10)
	nom_ciudad = models.CharField(max_length=100)
	zona_turistica = models.CharField(max_length=10, null=True)

	def __str__(self):
			texto = '{0}-{1}-{2}-{3}'
			return texto.format(self.provincia, self.nom_ciudad, self.cod_Postal, self.zona_turistica)

class Lugares_Turisticos(models.Model):
	zona_turistica = models.ForeignKey(Ciudad,  on_delete=models.SET_NULL, null=True, related_name="zona") 
	atractivos = models.TextField()
	descripcion = models.TextField(max_length=500)
	clalificacion = models.CharField(max_length=2)
	ubicacion = models.CharField(max_length=100)
	recomendaciones = models.TextField(max_length=500)

	def __str__(self):
		texto = '{0}-{1}-{2}-{3}-{4}-{5}'
		return texto.format( self.zona_turistica, self.atractivos, self.descripcion, self.calificacion, self.ubicación, self.recomendaciones)



	






