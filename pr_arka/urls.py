from django.contrib import admin
from django.urls import path, include  # <-- Asegúrate de importar 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_Liseth.urls')),  # <-- Esto conecta las rutas de tu app a la raíz del sitio
]