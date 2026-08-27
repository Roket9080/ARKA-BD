from django.contrib import admin
from django.urls import path, include  # <-- 1. Asegúrate de importar 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_Gomez.urls')),  # <-- 2. Conecta las rutas de tu app aquí
]