from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_miguel.urls')),
    path('', include('app_Gomez.urls')),
    path('', include('app_Liseth.urls')),
    path('', include("app_Alejandro_07.urls")),
    path('', include('app_cristian.urls')),
    path('', include('app_martinez.urls')),
    path('registro/', include('app_sebas.urls')),
    path('chat/', include('app_chat.urls')),
    
]
