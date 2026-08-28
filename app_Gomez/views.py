from django.shortcuts import render
from .models import AtencionMedica, CasoRiesgo

# 1. Vista para el Requerimiento 11 (Informes de Atención)
def ver_informe_atencion(request):
    # 1. Si el usuario envía el formulario desde la página, guardamos el registro
    if request.method == 'POST':
        tipo_atencion = request.POST.get('tipo_atencion')
        profesional = request.POST.get('profesional')
        zona = request.POST.get('zona')
        fecha = request.POST.get('fecha_inicio') # Usamos la fecha ingresada en el formulario

        # Si los campos esenciales no están vacíos, los guardamos en la base de datos
        if tipo_atencion and profesional and fecha:
            AtencionMedica.objects.create(
                tipo_atencion=tipo_atencion,
                profesional=profesional,
                municipio=zona if zona else 'Popayán',
                fecha=fecha,
                cantidad=1
            )

    # 2. Consultamos todas las atenciones para mostrarlas en la tabla de la página
    atenciones = AtencionMedica.objects.all().order_by('-id') # Del más reciente al más antiguo

    return render(request, 'app_Gomez/informe_atencion.html', {'atenciones': atenciones})


# 2. Vista para el Requerimiento 12 (Reportes de Suicidio)
def ver_reporte_suicidio(request):
    if request.method == 'POST':
        # Capturamos los datos del formulario de suicidio
        nivel_riesgo = request.POST.get('nivel_riesgo')
        estado_caso = request.POST.get('estado_caso')
        fecha_registro = request.POST.get('fecha_inicio')
        rango_edad = request.POST.get('rango_edad')

        # Convertimos el rango de edad del select en un número para la base de datos
        edad_map = {'12-17': 15, '18-28': 22, '29-59': 35, '60': 65}
        edad_estimada = edad_map.get(rango_edad, 25)

        # Si hay datos válidos, los guardamos en SQLite
        if nivel_riesgo and estado_caso and fecha_registro:
            CasoRiesgo.objects.create(
                edad=edad_estimada,
                nivel_riesgo=nivel_riesgo,
                estado_caso=estado_caso,
                fecha_registro=fecha_registro
            )

    # Consultamos los casos para mostrarlos en la tabla de la página
    casos = CasoRiesgo.objects.all().order_by('-id')
    return render(request, 'app_Gomez/reporte_suicidio.html', {'casos': casos})