from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Delegamos TODAS las rutas del proyecto a la app_informes
    path('', include('app_informes.urls')),
]