from django.urls import path

from . import views


urlpatterns = [

    path(
        "evaluacion/",
        views.crear_evaluacion,
        name="crear_evaluacion"
    ),

    path(
        "evaluaciones/",
        views.listar_evaluaciones,
        name="listar_evaluaciones"
    ),

    path(
        "ubicacion/",
        views.registrar_ubicacion,
        name="registrar_ubicacion"
    ),

    path(
        "ubicaciones/",
        views.listar_ubicaciones,
        name="listar_ubicaciones"
    ),

]