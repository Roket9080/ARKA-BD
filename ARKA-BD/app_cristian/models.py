from django.db import models

class AtencionSalud(models.Model):
    # ENTRADAS
    solicitud_usuario = models.TextField(verbose_name="Solicitud del usuario")
    historia_clinica = models.TextField(verbose_name="Información clínica básica / Antecedentes")
    evaluacion_inicial = models.TextField(verbose_name="Resultados de evaluaciones iniciales")

    # SALIDAS
    reporte_valoracion = models.TextField(verbose_name="Reporte de valoración psicológica o en salud")
    plan_tratamiento = models.TextField(verbose_name="Plan de intervención o tratamiento")
    estrategias_prevencion = models.TextField(verbose_name="Estrategias de prevención y recomendaciones")
    
    # METADATA
    fecha_registro = models.DateTimeField(auto_now_add=True)
    profesional = models.CharField(max_length=150, verbose_name="Profesional a cargo")

    def __str__(self):
        return f"Atención {self.id} - {self.profesional}"