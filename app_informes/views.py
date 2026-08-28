from django.shortcuts import render, redirect, get_object_or_404
from .models import InformeAtencion

def lista_informes(request):
    informes = InformeAtencion.objects.all()
    return render(request, 'app_informes/lista_informes.html', {'informes': informes})

def crear_informe(request):
    if request.method == 'POST':
        nuevo = InformeAtencion()
        nuevo.tipo_atencion = request.POST.get('tipo_atencion')
        nuevo.profesional = request.POST.get('profesional')
        nuevo.zona_geografica = request.POST.get('zona_geografica')
        nuevo.usuario = request.POST.get('usuario')
        nuevo.resumen = request.POST.get('resumen')
        nuevo.save()
        return redirect('lista_informes')
    return render(request, 'app_informes/crear_informe.html')

def editar_informe(request, pk):
    informe = get_object_or_404(InformeAtencion, pk=pk)
    if request.method == 'POST':
        informe.tipo_atencion = request.POST.get('tipo_atencion')
        informe.profesional = request.POST.get('profesional')
        informe.zona_geografica = request.POST.get('zona_geografica')
        informe.usuario = request.POST.get('usuario')
        informe.resumen = request.POST.get('resumen')
        informe.save()
        return redirect('lista_informes')
    return render(request, 'app_informes/crear_informe.html', {'informe': informe})

def eliminar_informe(request, pk):
    informe = get_object_or_404(InformeAtencion, pk=pk)
    if request.method == 'POST':
        informe.delete()
        return redirect('lista_informes')
    return render(request, 'app_informes/eliminar_informe.html', {'informe': informe})