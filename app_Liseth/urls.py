from django.urls import path
from . import views

urlpatterns = [
    path('revision-secretaria/', views.ver_revision_secretaria, name='revision_secretaria'),
    path('reportes-secretaria/', views.ver_reportes_secretaria, name='reportes_secretaria'),
]