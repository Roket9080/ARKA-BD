from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='registro_profesional', permanent=False)),
    path('registro/', include('app_sebas.urls')),
    path('chat/', include('app_chat.urls')),
]