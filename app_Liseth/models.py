from django.db import models

# Modelo para el RF-NU-0013 (Revisión Secretaría)
class RevisionSecretaria(models.Model):
    identificador = models.CharField(max_length=20, default="RF-NU-0013")
    usuario_en_riesgo = models.CharField(max_length=150)
    informe_asociado = models.CharField(max_length=200)
    estado_revision = models.CharField(max_length=50, default="Pendiente")
    observaciones = models.TextField(blank=True, null=True)
    fecha_revision = models.DateField()

    def __str__(self):
        return f"Revisión {self.id} - {self.usuario_en_riesgo}"


# Modelo para el RF-NU-0014 (Reportes y Estadísticas de Riesgo)
class ReporteSecretariaRiesgo(models.Model):
    identificador = models.CharField(max_length=20, default="RF-NU-0014")
    nivel_riesgo = models.CharField(max_length=50) # Bajo, medio, alto, crítico
    tipo_intervencion = models.CharField(max_length=150) # Apoyo psicológico, derivación, llamada, videollamada
    fuente_reporte = models.CharField(max_length=100) # Autoevaluación, profesional, etc.
    zona_territorial = models.CharField(max_length=100, default="Popayán")
    fecha_registro = models.DateField()

    def __str__(self):
        return f"Reporte {self.id} - Riesgo: {self.nivel_riesgo}"

# Create your models here.
