from django.urls import path
from .views import ver_informe_atencion, ver_reporte_suicidio

urlpatterns = [
    path('informes-atencion/', ver_informe_atencion, name='informes_atencion'),
    path('reportes-suicidio/', ver_reporte_suicidio, name='reportes_suicidio'),
]