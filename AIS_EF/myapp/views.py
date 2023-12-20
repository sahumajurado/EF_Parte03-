from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def integrantes(request):
    return render(request, 'integrantes.html')


def v_crear_producto(request):
    return render(request, 'v_crear_producto.html')


def v_crear_curso(request):
    return render(request, 'v_crear_curso.html')
