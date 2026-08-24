from django.shortcuts import render, redirect
from .models import AtencionSalud

def requerimiento1(request):
    if request.method == 'POST':
        # Captura de Entradas
        solicitud = request.POST.get('solicitud')
        historia = request.POST.get('historia')
        evaluacion = request.POST.get('evaluacion')
        
        # Captura de Salidas
        reporte = request.POST.get('reporte')
        plan = request.POST.get('plan')
        estrategias = request.POST.get('estrategias')
        profesional = request.POST.get('profesional')

        # Guardar en Base de Datos
        AtencionSalud.objects.create(
            solicitud_usuario=solicitud,
            historia_clinica=historia,
            evaluacion_inicial=evaluacion,
            reporte_valoracion=reporte,
            plan_tratamiento=plan,
            estrategias_prevencion=estrategias,
            profesional=profesional
        )
        return redirect('requerimiento1')

    # Obtener registros para mostrar el historial
    registros = AtencionSalud.objects.all().order_by('-fecha_registro')
    return render(request, 'app_cristian/requerimiento1.html', {'registros': registros})