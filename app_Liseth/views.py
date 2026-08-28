from django.shortcuts import render
from .models import RevisionSecretaria, ReporteSecretariaRiesgo

# Vista para RF-NU-0013
def ver_revision_secretaria(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario_en_riesgo')
        informe = request.POST.get('informe_asociado')
        estado = request.POST.get('estado_revision')
        observaciones = request.POST.get('observaciones')
        fecha = request.POST.get('fecha_revision')

        if usuario and fecha:
            RevisionSecretaria.objects.create(
                usuario_en_riesgo=usuario,
                informe_asociado=informe if informe else 'Informe general',
                estado_revision=estado if estado else 'En proceso',
                observaciones=observaciones,
                fecha_revision=fecha
            )

    revisiones = RevisionSecretaria.objects.all().order_by('-id')
    return render(request, 'app_liseth/revision_secretaria.html', {'revisiones': revisiones})


# Vista para RF-NU-0014
def ver_reportes_secretaria(request):
    if request.method == 'POST':
        nivel = request.POST.get('nivel_riesgo')
        intervencion = request.POST.get('tipo_intervencion')
        fuente = request.POST.get('fuente_reporte')
        zona = request.POST.get('zona_territorial')
        fecha = request.POST.get('fecha_registro')

        if nivel and fecha:
            ReporteSecretariaRiesgo.objects.create(
                nivel_riesgo=nivel,
                tipo_intervencion=intervencion if intervencion else 'General',
                fuente_reporte=fuente if fuente else 'Autoevaluación',
                zona_territorial=zona if zona else 'Popayán',
                fecha_registro=fecha
            )

    # Lógica de filtrado opcional si buscan por nivel de riesgo en la interfaz
    filtro_riesgo = request.GET.get('filtro_riesgo')
    if filtro_riesgo:
        reportes = ReporteSecretariaRiesgo.objects.filter(nivel_riesgo__icontains=filtro_riesgo).order_by('-id')
    else:
        reportes = ReporteSecretariaRiesgo.objects.all().order_by('-id')

    return render(request, 'app_liseth/reportes_secretaria.html', {'reportes': reportes})