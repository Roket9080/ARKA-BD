from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Tu app gestiona el inicio, login, registro y la página principal
    path('', include('app_miguel.urls')),
    
    # Administración de Django
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    
    # Módulos de tus compañeros
    path('santiago/', include('app_Gomez.urls')),
    path('liseth/', include('app_Liseth.urls')),
    path('alejandro/', include("app_Alejandro_07.urls")),
    path('cristian/', include('app_cristian.urls')),
    path('martinez/', include('app_martinez.urls')),
    path('registro/', include('app_sebas.urls')), # O la app de Sebas
    path('chat/', include('app_chat.urls')),
]