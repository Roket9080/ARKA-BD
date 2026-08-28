from django.db import models

class InformeAtencion(models.Model):
    id_informe = models.AutoField(primary_key=True)
    fecha_atencion = models.DateTimeField(auto_now_add=True)
    tipo_atencion = models.CharField(max_length=100)  # Ej: Psicológica, Psiquiátrica
    profesional = models.CharField(max_length=100)    # Nombre del profesional
    zona_geografica = models.CharField(max_length=100) # Ej: Comuna 1, Comuna 2
    usuario = models.CharField(max_length=100)       # Nombre del usuario atendido
    resumen = models.TextField()                     # Resumen de la atención

    def __str__(self):
        return f"Informe #{self.id_informe} - {self.usuario}"