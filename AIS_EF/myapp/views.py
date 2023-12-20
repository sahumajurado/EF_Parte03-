from django.shortcuts import render, redirect
from .models import Producto, Curso


def index(request):
    return render(request, 'index.html')


def integrantes(request):
    return render(request, 'integrantes.html')


def v_crear_producto(request):
    return render(request, 'crear_productos.html')

def crear_producto(request):
    codigo = request.POST['codigo']
    nombre = request.POST['nombre']
    precio_compra = request.POST['precio_compra']
    precio_venta = request.POST['precio_venta']
    fecha_compra = request.POST['fecha_compra']
    estado = request.POST['estado']
    producto = Producto.objects.create(codigo=codigo, nombre=nombre,precio_compra=precio_compra,
    precio_venta=precio_venta, fecha_compra=fecha_compra,
    estado=estado)
    return redirect('/v_crear_producto')


def v_crear_curso(request):
    return render(request, 'crear_curso.html')

def crear_curso(request):
    codigo= request.POST['cod']
    nombre= request.POST['nombre']
    horas=request.POST['horas']
    creditos=request.POST['creditos']
    fecha_registro=request.POST['fecha_registro']
    estado=request.POST['estado']
    curso = Curso.objects.create(codigo=codigo, nombre=nombre, horas=horas, creditos=creditos, 
    fecha_registro=fecha_registro, estado=estado)
    return redirect('/v_crear_curso')
