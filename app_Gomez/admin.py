from django.contrib import admin
from .models import AtencionMedica, CasoRiesgo

# Registramos los modelos para que aparezcan en el panel de administración
admin.site.register(AtencionMedica)
admin.site.register(CasoRiesgo)