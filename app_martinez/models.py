from django.db import models
from django.contrib.auth.models import User

class MensajeChat(models.Model):
    TIPO_CHAT_CHOICES = [
        ('GRUPAL', 'Chat Grupal'),
        ('PERSONAL', 'Chat Personal'),
    ]

    emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='mensajes_recibidos')
    tipo_chat = models.CharField(max_length=10, choices=TIPO_CHAT_CHOICES, default='GRUPAL')
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.emisor.username} ({self.tipo_chat}): {self.contenido[:20]}"