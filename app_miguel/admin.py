from django.contrib import admin
from .models import Requerimiento

@admin.register(Requerimiento)
class RequerimientoAdmin(admin.ModelAdmin):
    # 1. Columnas que se verán en la tabla principal del panel
    list_display = ('identificador', 'nombre', 'rol', 'creado_en')
    
    # 2. Panel de filtros lateral a la derecha
    list_filter = ('rol', 'creado_en') 
    
    # 3. Barra de búsqueda superior
    search_fields = ('identificador', 'nombre', 'descripcion')
    
    # 4. Ordenar para que los requerimientos más recientes salgan primero
    ordering = ('-creado_en',)