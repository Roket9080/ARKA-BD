from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', include('app_sebas.urls')),
    path('chat/', include('app_chat.urls')),
]