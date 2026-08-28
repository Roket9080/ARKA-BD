from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_informes, name='lista_informes'),
    path('crear/', views.crear_informe, name='crear_informe'),
    path('editar/<int:pk>/', views.editar_informe, name='editar_informe'),
    path('eliminar/<int:pk>/', views.eliminar_informe, name='eliminar_informe'),
]