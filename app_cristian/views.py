from django.shortcuts import render


def index(request):
    return render(request, 'app_cristian/index.html')


def requerimiento1(request):
    return render(request, 'app_cristian/requerimiento1.html')


def requerimiento2(request):
    return render(request, 'app_cristian/requerimiento2.html')