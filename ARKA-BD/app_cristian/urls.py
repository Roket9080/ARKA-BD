from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('atencion-salud/',
         views.requerimiento1,
         name='requerimiento1'),

    path('emergencia/',
         views.requerimiento2,
         name='requerimiento2'),
]