from django.shortcuts import render, redirect, get_object_or_404
from .models import Profesional

def lista_profesional(request):
    profesionales = Profesional.objects.all()
    return render(request, 'app_sebas/lista_profesional.html', {'profesionales': profesionales})

def registro_profesional(request):
    if request.method == 'POST':
        nuevo = Profesional()
        nuevo.identificador = request.POST.get('identificador')
        nuevo.contrasena = request.POST.get('contrasena')
        nuevo.nombres = request.POST.get('nombres')
        nuevo.apellidos = request.POST.get('apellidos')
        nuevo.correo = request.POST.get('correo')
        nuevo.telefono = request.POST.get('telefono')
        nuevo.contacto_emergencia = request.POST.get('contacto_emergencia')
        nuevo.disponibilidad_horarios = request.POST.get('disponibilidad_horarios')
        nuevo.direccion = request.POST.get('direccion')
        nuevo.save()
        return redirect('lista_profesional')
    return render(request, 'app_sebas/registro_profesional.html')

def editar_profesional(request, pk):
    profesional = get_object_or_404(Profesional, pk=pk)
    if request.method == 'POST':
        profesional.identificador = request.POST.get('identificador')
        profesional.contrasena = request.POST.get('contrasena')
        profesional.nombres = request.POST.get('nombres')
        profesional.apellidos = request.POST.get('apellidos')
        profesional.correo = request.POST.get('correo')
        profesional.telefono = request.POST.get('telefono')
        profesional.contacto_emergencia = request.POST.get('contacto_emergencia')
        profesional.disponibilidad_horarios = request.POST.get('disponibilidad_horarios')
        profesional.direccion = request.POST.get('direccion')
        profesional.save()
        return redirect('lista_profesional')
    return render(request, 'app_sebas/registro_profesional.html', {'profesional': profesional})

def eliminar_profesional(request, pk):
    profesional = get_object_or_404(Profesional, pk=pk)
    if request.method == 'POST':
        profesional.delete()
        return redirect('lista_profesional')
    return render(request, 'app_sebas/eliminar_profesional.html', {'profesional': profesional})