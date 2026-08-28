from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_chats, name='lista_chats'),
    path('crear/', views.crear_chat, name='crear_chat'),
    path('<int:pk>/', views.ver_chat, name='ver_chat'),
]