from django.contrib import admin
from .models import Helado, MateriaPrima, MateriaPrima_Helado, Maquina, MaquinaHelado

class MateriaPrima_HeladoInLine(admin.TabularInline):
    model = MateriaPrima_Helado
    extra = 3

class HeladoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nombre',               {'fields': ['nombre']}),
        ('Precio', {'fields': ['precio']}),
    ]
    inlines = [MateriaPrima_HeladoInLine]
    list_filter = ['precio']

admin.site.register(Helado, HeladoAdmin)
admin.site.register(MateriaPrima)
admin.site.register(Maquina)
admin.site.register(MaquinaHelado)
