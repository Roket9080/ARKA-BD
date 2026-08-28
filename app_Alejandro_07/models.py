from django.db import models


class EvaluacionEmocional(models.Model):
    usuario = models.CharField(max_length=100)
    profesional = models.CharField(max_length=100)
    estado_afectivo = models.CharField(max_length=100)
    nivel_riesgo = models.CharField(max_length=50)
    necesidades_detectadas = models.TextField()
    observaciones = models.TextField(blank=True, null=True)
    recomendaciones = models.TextField(blank=True, null=True)
    fecha_evaluacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Evaluación - {self.usuario}"


class UbicacionPaciente(models.Model):
    paciente = models.CharField(max_length=100)
    latitud = models.DecimalField(max_digits=10, decimal_places=7)
    longitud = models.DecimalField(max_digits=10, decimal_places=7)
    autorizacion = models.BooleanField(default=False)
    motivo = models.CharField(max_length=200, blank=True, null=True)
    fecha_ubicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ubicación - {self.paciente}"