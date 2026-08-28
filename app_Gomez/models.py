from django.db import models

# Modelo para el RF-NU-0011 (Informes de Atención)
class AtencionMedica(models.Model):
    TIPO_ATENCION_CHOICES = [
        ('general', 'Medicina General'),
        ('urgencias', 'Urgencias'),
        ('especializada', 'Consulta Especializada'),
    ]
    PROFESIONAL_CHOICES = [
        ('dr_perez', 'Dr. Carlos Pérez'),
        ('dra_gomez', 'Dra. Ana Gómez'),
    ]

    cantidad = models.IntegerField(default=1)
    tipo_atencion = models.CharField(max_length=50, choices=TIPO_ATENCION_CHOICES)
    profesional = models.CharField(max_length=50, choices=PROFESIONAL_CHOICES)
    municipio = models.CharField(max_length=100, default='Popayán')
    fecha = models.DateField()

    def __str__(self):
        return f"Atención {self.id} - {self.tipo_atencion}"


# Modelo para el RF-NU-0012 (Casos de Riesgo de Suicidio)
class CasoRiesgo(models.Model):
    RIESGO_CHOICES = [
        ('critico', 'Crítico'),
        ('alto', 'Alto'),
        ('medio', 'Medio'),
        ('bajo', 'Bajo'),
    ]
    ESTADO_CHOICES = [
        ('abierto', 'Abierto'),
        ('seguimiento', 'En Seguimiento'),
        ('cerrado', 'Cerrado'),
    ]

    edad = models.IntegerField()
    nivel_riesgo = models.CharField(max_length=20, choices=RIESGO_CHOICES)
    estado_caso = models.CharField(max_length=30, choices=ESTADO_CHOICES)
    fecha_registro = models.DateField()

    def __str__(self):
        return f"Caso #{self.id} - {self.nivel_riesgo}"