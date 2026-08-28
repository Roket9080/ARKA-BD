from django.db import models

class Profesional(models.Model):
    id_profesional = models.AutoField(primary_key=True)
    identificador = models.CharField(max_length=100, unique=True)
    contrasena = models.CharField(max_length=255)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    contacto_emergencia = models.CharField(max_length=100)
    disponibilidad_horarios = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"