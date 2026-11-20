from django.urls import path
from . import views

urlpatterns = [
    # Ruta raíz: http://127.0.0.1:8000/ (Carga tu página de inicio)
    path('', views.pagina_inicio, name='inicio'),
    
    # Ruta para la lista: http://127.0.0.1:8000/lista/
    path('lista/', views.lista_informes, name='lista_informes'),
    
    # Ruta para crear: http://127.0.0.1:8000/crear/
    path('crear/', views.crear_informe, name='crear_informe'),
    
    # Rutas con ID para editar y eliminar
    path('editar/<int:pk>/', views.editar_informe, name='editar_informe'),
    path('eliminar/<int:pk>/', views.eliminar_informe, name='eliminar_informe'),
]