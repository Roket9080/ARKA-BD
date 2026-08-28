from django.db import models
from app_sebas.models import Profesional

class ChatGrupal(models.Model):
    id_chat = models.AutoField(primary_key=True)
    nombre_grupo = models.CharField(max_length=100)
    creado_por = models.ForeignKey(Profesional, on_delete=models.CASCADE, related_name='chats_creados')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_grupo

class MensajeChat(models.Model):
    id_mensaje = models.AutoField(primary_key=True)
    chat = models.ForeignKey(ChatGrupal, on_delete=models.CASCADE, related_name='mensajes')
    autor = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.autor} en {self.chat}"