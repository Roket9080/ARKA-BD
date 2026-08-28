from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import MensajeChat

@login_required
def chat_grupal(request):
    if request.method == 'POST':
        texto = request.POST.get('mensaje')
        if texto:
            MensajeChat.objects.create(
                emisor=request.user,
                tipo_chat='GRUPAL',
                contenido=texto
            )
            return redirect('chat_grupal')

    mensajes = MensajeChat.objects.filter(tipo_chat='GRUPAL').order_by('fecha_envio')
    return render(request, 'chat_grupal.html', {'mensajes': mensajes})

@login_required
def chat_personal(request, usuario_id):
    receptor = User.objects.get(id=usuario_id)
    if request.method == 'POST':
        texto = request.POST.get('mensaje')
        if texto:
            MensajeChat.objects.create(
                emisor=request.user,
                receptor=receptor,
                tipo_chat='PERSONAL',
                contenido=texto
            )
            return redirect('chat_personal', usuario_id=usuario_id)

    mensajes = MensajeChat.objects.filter(
        tipo_chat='PERSONAL',
        emisor__in=[request.user, receptor],
        receptor__in=[request.user, receptor]
    ).order_by('fecha_envio')

    return render(request, 'chat_personal.html', {'mensajes': mensajes, 'receptor': receptor})