from django.urls import path
from . import views

urlpatterns = [
    path('chat-grupal/', views.chat_grupal, name='chat_grupal'),
    path('chat-personal/<int:usuario_id>/', views.chat_personal, name='chat_personal'),
]
