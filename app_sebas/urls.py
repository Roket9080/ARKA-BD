from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_profesional, name='lista_profesional'),
    path('registro/', views.registro_profesional, name='registro_profesional'),
    path('editar/<int:pk>/', views.editar_profesional, name='editar_profesional'),
    path('eliminar/<int:pk>/', views.eliminar_profesional, name='eliminar_profesional'),
]