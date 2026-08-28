from django.shortcuts import render, redirect, get_object_or_404
from .models import ChatGrupal, MensajeChat
from app_sebas.models import Profesional

def lista_chats(request):
    chats = ChatGrupal.objects.all()
    return render(request, 'app_chat/lista_chats.html', {'chats': chats})

def crear_chat(request):
    if request.method == 'POST':
        nuevo_chat = ChatGrupal()
        nuevo_chat.nombre_grupo = request.POST.get('nombre_grupo')
        nuevo_chat.creado_por_id = request.POST.get('creado_por_id')
        nuevo_chat.save()
        return redirect('lista_chats')
    profesionales = Profesional.objects.all()
    return render(request, 'app_chat/crear_chat.html', {'profesionales': profesionales})

def ver_chat(request, pk):
    chat = get_object_or_404(ChatGrupal, pk=pk)
    mensajes = MensajeChat.objects.filter(chat=chat).order_by('fecha_envio')
    if request.method == 'POST':
        nuevo_mensaje = MensajeChat()
        nuevo_mensaje.chat = chat
        nuevo_mensaje.autor_id = request.POST.get('autor_id')
        nuevo_mensaje.contenido = request.POST.get('contenido')
        nuevo_mensaje.save()
        return redirect('ver_chat', pk=pk)
    profesionales = Profesional.objects.all()
    return render(request, 'app_chat/ver_chat.html', {'chat': chat, 'mensajes': mensajes, 'profesionales': profissionais})