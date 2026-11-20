from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_view, name='inicio'),
    path("registrarse/", views.registro_view, name="registrarse"),# La landing page pública
    path('login/', views.login_view, name='login'),               # El login
    path('principal/', views.principal_view, name='principal'),
    path('chat/', views.chat_view, name='chat'),# <--- La nueva página principal/dashboard
    path('logout/', views.logout_view, name='logout'),             # Para cerrar sesión
    path('usuarios/', views.usuarios_view, name='usuarios'),       # Formulario de registro (RF-NU-001)
    path('requerimientos/', views.requerimientos_view, name='requerimientos'),
    path('requerimientos2/', views.requerimientos2_view, name='requerimientos2'),
]