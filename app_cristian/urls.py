from django.urls import path
from . import views

urlpatterns = [
    path('requerimiento1/', views.requerimiento1, name='requerimiento1'),
    path('requerimiento2/', views.requerimiento2, name='requerimiento2'),
]