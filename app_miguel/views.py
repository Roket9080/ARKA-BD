from django.shortcuts import render, redirect
from .models import UsuarioArka, Requerimiento

def usuarios_view(request):
    if request.method == 'POST':
        UsuarioArka.objects.create(
            identificador_unico=request.POST.get('identificador_unico'),
            password=request.POST.get('password'),
            nombres=request.POST.get('nombres'),
            apellidos=request.POST.get('apellidos'),
            correo=request.POST.get('correo'),
            telefono=request.POST.get('telefono'),
            contacto_emergencia=request.POST.get('contacto_emergencia'),
            direccion=request.POST.get('direccion')
        )
        return redirect('usuarios')

    registros = UsuarioArka.objects.all().order_by('-id')
    return render(request, 'app_miguel/usuarios.html', {'registros': registros})


def requerimientos_view(request):
    if request.method == 'POST':
        Requerimiento.objects.create(
            identificador=request.POST.get('identificador'),
            nombre=request.POST.get('nombre'),
            descripcion=request.POST.get('descripcion'),
            entradas=request.POST.get('entradas'),
            salidas=request.POST.get('salidas'),
            criterios_aceptacion=request.POST.get('criterios_aceptacion'),
            rol=request.POST.get('rol')
        )
        return redirect('requerimientos')

    # Si la tabla está vacía, precarga automáticamente el RF-NU-002
    if not Requerimiento.objects.exists():
        Requerimiento.objects.create(
            identificador="RF-NU-002",
            nombre="Acceso a chat bot",
            descripcion="Ofrece a los usuarios acceder a un chatbot integrado en la aplicación brindando soporte en tiempo real y respuestas rápidas a consultas comunes",
            entradas="• Preguntas y mensajes escritos por el usuario\n• solicitud de ayuda",
            salidas="• Respuesta rápida del chatbot a la pregunta\n• orientación o redirección",
            criterios_aceptacion="• El chat debe estar accesible desde la aplicación\n• El chat debe tener respuestas rápidas\n• Debe tener lenguaje claro sencillo y coherente",
            rol="Usuario, Administración, y profesionales"
        )

    registros = Requerimiento.objects.all().order_by('-id')
    return render(request, 'requerimientos.html', {'registros': registros})