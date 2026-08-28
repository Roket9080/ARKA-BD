from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('miguel/', include('app_miguel.urls')),
    path('santiago/', include('app_Gomez.urls')),
    path('liseth/', include('app_Liseth.urls')),
    path('alejandro/', include("app_Alejandro_07.urls")),
    path('cristian/', include('app_cristian.urls')),
    path('martinez/', include('app_martinez.urls')),
    path('registro/', include('app_sebas.urls')),
    path('chat/', include('app_chat.urls')),
    
]
