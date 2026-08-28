from django.shortcuts import render, redirect

from .models import (
    EvaluacionEmocional,
    UbicacionPaciente
)


def crear_evaluacion(request):

    if request.method == "POST":

        EvaluacionEmocional.objects.create(
            usuario=request.POST.get("usuario"),
            profesional=request.POST.get("profesional"),
            estado_afectivo=request.POST.get("estado_afectivo"),
            nivel_riesgo=request.POST.get("nivel_riesgo"),
            necesidades_detectadas=request.POST.get(
                "necesidades_detectadas"
            ),
            observaciones=request.POST.get("observaciones"),
            recomendaciones=request.POST.get("recomendaciones")
        )

        return redirect("listar_evaluaciones")

    return render(
        request,
        "Alejandro_07/evaluacion_emocional.html"
    )


def listar_evaluaciones(request):

    evaluaciones = EvaluacionEmocional.objects.all()

    return render(
        request,
        "Alejandro_07/listar_evaluaciones.html",
        {
            "evaluaciones": evaluaciones
        }
    )


def registrar_ubicacion(request):

    if request.method == "POST":

        autorizacion = request.POST.get("autorizacion")

        UbicacionPaciente.objects.create(
            paciente=request.POST.get("paciente"),
            latitud=request.POST.get("latitud"),
            longitud=request.POST.get("longitud"),
            autorizacion=True if autorizacion else False,
            motivo=request.POST.get("motivo")
        )

        return redirect("listar_ubicaciones")

    return render(
        request,
        "Alejandro_07/ubicacion_paciente.html"
    )


def listar_ubicaciones(request):
    ubicaciones = UbicacionPaciente.objects.all()

    return render(
        request,
        "Alejandro_07/listar_ubicaciones.html",
        {
            "ubicaciones": ubicaciones
        }
    )