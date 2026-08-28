from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AtencionSalud, ConfiguracionEmergencia, RegistroLlamadaEmergencia

def requerimiento1(request):
    if request.method == 'POST':
        solicitud = request.POST.get('solicitud')
        historia = request.POST.get('historia')
        evaluacion = request.POST.get('evaluacion')
        reporte = request.POST.get('reporte')
        plan = request.POST.get('plan')
        estrategias = request.POST.get('estrategias')
        profesional = request.POST.get('profesional')

        AtencionSalud.objects.create(
            solicitud_usuario=solicitud, historia_clinica=historia,
            evaluacion_inicial=evaluacion, reporte_valoracion=reporte,
            plan_tratamiento=plan, estrategias_prevencion=estrategias,
            profesional=profesional
        )
        return redirect('requerimiento1')

    registros = AtencionSalud.objects.all().order_by('-fecha_registro')
    return render(request, 'app_cristian/requerimiento1.html', {'registros': registros})

# NUEVA VISTA: Requerimiento 2
def requerimiento2(request):
    config, _ = ConfiguracionEmergencia.objects.get_or_create(id=1)

    if request.method == 'POST':
        # Cambio de número de emergencia por el administrador
        if 'guardar_config' in request.POST:
            nuevo_num = request.POST.get('numero_emergencia')
            config.numero_emergencia = nuevo_num
            config.save()
            messages.success(request, "Número de emergencia actualizado correctamente.")
        
        # Acción del botón de emergencia
        elif 'activar_emergencia' in request.POST:
            if config.activo:
                RegistroLlamadaEmergencia.objects.create(
                    numero_marcado=config.numero_emergencia,
                    estado="Efectiva"
                )
                messages.success(request, f"¡Llamada iniciada con éxito a la línea {config.numero_emergencia}!")
            else:
                messages.error(request, "Error: La línea de emergencia no está disponible actualmente.")

        return redirect('requerimiento2')

    historial = RegistroLlamadaEmergencia.objects.all().order_by('-fecha_hora')
    return render(request, 'app_cristian/requerimiento2.html', {
        'config': config,
        'historial': historial
    })