from django.db import models

class UsuarioArka(models.Model):
    identificador_unico = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  # Para la contraseña
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    contacto_emergencia = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.identificador_unico} - {self.nombres} {self.apellidos}"
    
    
class Requerimiento(models.Model):
    identificador = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    entradas = models.TextField()
    salidas = models.TextField()
    criterios_aceptacion = models.TextField()
    rol = models.CharField(max_length=150)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.identificador} - {self.nombre}"