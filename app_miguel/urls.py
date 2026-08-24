from django.urls import path
from . import views

urlpatterns = [
    path('requerimientos/', views.requerimientos_view, name='requerimientos'),
    path('usuarios/', views.usuarios_view, name='usuarios'),
]