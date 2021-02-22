from django.contrib import admin
from .models import *

# Register your models here.
"""@admin.register(Paises)
class PaisesAdmin(admin.ModelAdmin):
	search_fields = ('codigo', 'pais')

	def datos(self, obj):
		return obj.nombre.upper()

	datos.short_description = 'XYA'
"""


@admin.register(Paises, Provincia, Ciudad, Lugares_Turisticos)
class PaisesAdmin(admin.ModelAdmin):
    pass


"""admin.site.register(Paises)
admin.site.register(Provincia)
admin.site.register(Ciudad)
"""