from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import Requerimiento, UsuarioArka
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioForm


def inicio_view(request):
    return render(request, 'app_miguel/inicio.html')

def login_view(request):
    # Si el usuario ya está logueado y vuelve a /login/, lo mandamos directo al panel
    if request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        user_input = request.POST.get('username')
        pass_input = request.POST.get('password')

        user = authenticate(request, username=user_input, password=pass_input)
        if user is not None:
            # 1. Mantiene la sesión activa guardando la cookie
            login(request, user)
            # 2. Transiciona inmediatamente a la página principal
            return redirect('principal')
        else:
            return render(request, 'app_miguel/login.html', {
                'error': 'Usuario o contraseña incorrectos'
            })

    return render(request, 'app_miguel/login.html')

# Vista protegida: solo carga si existe la sesión activa
@login_required(login_url='login')
def principal_view(request):
    return render(request, 'app_miguel/principal.html', {'usuario': request.user})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def chat_view(request):
    return render(request, 'app_miguel/chat.html', {'usuario': request.user})

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
            direccion=request.POST.get('direccion'),
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
            rol=request.POST.get('rol'),
        )
        return redirect('requerimientos')

    # Si la tabla está vacía, precarga automáticamente el RF-NU-002
    if not Requerimiento.objects.exists():
        Requerimiento.objects.create(
            identificador='RF-NU-002',
            nombre='Acceso a chat bot',
            descripcion=(
                'Ofrece a los usuarios acceder a un chatbot integrado en la '
                'aplicación brindando soporte en tiempo real y respuestas rápidas '
                'a consultas comunes'
            ),
            entradas='Preguntas y mensajes escritos por el usuario\nSolicitud de ayuda',
            salidas='Respuesta rápida del chatbot a la pregunta\nOrientación o redirección',
            criterios_aceptacion=(
                'El chat debe estar accesible desde la aplicación\n'
                'El chat debe tener respuestas rápidas\n'
                'Debe tener lenguaje claro sencillo y coherente'
            ),
            rol='Usuario, Administración, y profesionales',
        )

    registros = Requerimiento.objects.all().order_by('-id')
    return render(request, 'app_miguel/requerimiento1.html', {'registros': registros})


def requerimientos2_view(request):
    if request.method == 'POST':
        Requerimiento.objects.create(
            identificador=request.POST.get('identificador'),
            nombre=request.POST.get('nombre'),
            descripcion=request.POST.get('descripcion'),
            entradas=request.POST.get('entradas'),
            salidas=request.POST.get('salidas'),
            criterios_aceptacion=request.POST.get('criterios_aceptacion'),
            rol=request.POST.get('rol'),
        )
        return redirect('requerimientos2')

    # Si la tabla está vacía, precarga automáticamente el registro base
    if not Requerimiento.objects.exists():
        Requerimiento.objects.create(
            identificador='RF-NU-002',
            nombre='Acceso a chat bot',
            descripcion=(
                'Ofrece a los usuarios acceder a un chatbot integrado en la '
                'aplicación brindando soporte en tiempo real y respuestas rápidas '
                'a consultas comunes'
            ),
            entradas='Preguntas y mensajes escritos por el usuario\nSolicitud de ayuda',
            salidas='Respuesta rápida del chatbot a la pregunta\nOrientación o redirección',
            criterios_aceptacion=(
                'El chat debe estar accesible desde la aplicación\n'
                'El chat debe tener respuestas rápidas\n'
                'Debe tener lenguaje claro sencillo y coherente'
            ),
            rol='Usuario, Administración, y profesionales',
        )

    registros = Requerimiento.objects.all().order_by('-id')
    return render(request, 'app_miguel/requerimientos2.html', {'registros': registros})

def registro_view(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario, backend='django.contrib.auth.backends.ModelBackend')
            return redirect("principal")  # Cambia "inicio" por el name de tu URL principal
    else:
        form = RegistroUsuarioForm()

    return render(request, "app_miguel/registro.html", {"form": form})