from django.urls import path
from . import views

urlpatterns = [
    path('requerimiento1/', views.requerimiento1, name='requerimiento1'),
]