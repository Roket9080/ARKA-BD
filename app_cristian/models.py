from django.db import models

# Requerimiento 1 (No se modifica)
class AtencionSalud(models.Model):
    solicitud_usuario = models.TextField(verbose_name="Solicitud del usuario")
    historia_clinica = models.TextField(verbose_name="Información clínica básica / Antecedentes")
    evaluacion_inicial = models.TextField(verbose_name="Resultados de evaluaciones iniciales")
    reporte_valoracion = models.TextField(verbose_name="Reporte de valoración psicológica o en salud")
    plan_tratamiento = models.TextField(verbose_name="Plan de intervención o tratamiento")
    estrategias_prevencion = models.TextField(verbose_name="Estrategias de prevención y recomendaciones")
    fecha_registro = models.DateTimeField(auto_now_add=True)
    profesional = models.CharField(max_length=150, verbose_name="Profesional a cargo")

    def __str__(self):
        return f"Atención {self.id} - {self.profesional}"

# Requerimiento 2: Configuración del Número de Emergencia
class ConfiguracionEmergencia(models.Model):
    numero_emergencia = models.CharField(max_length=20, default="123", verbose_name="Número de Línea de Emergencia")
    activo = models.BooleanField(default=True, verbose_name="Línea Disponible")

    def __str__(self):
        return f"Línea de emergencia: {self.numero_emergencia}"

# Requerimiento 2: Historial de Llamadas
class RegistroLlamadaEmergencia(models.Model):
    fecha_hora = models.DateTimeField(auto_now_add=True)
    numero_marcado = models.CharField(max_length=20)
    estado = models.CharField(max_length=50, default="Efectiva")

    def __str__(self):
        return f"Llamada a {self.numero_marcado} el {self.fecha_hora.strftime('%d/%m/%Y %H:%M')}"