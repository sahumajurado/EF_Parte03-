
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('integrantes/', views.integrantes, name='integrantes'),
    path('v_crear_producto/', views.v_crear_producto, name='v_crear_producto'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('v_crear_curso/', views.v_crear_curso, name='v_crear_curso'),
    path('crear_curso/', views.crear_curso, name='crear_curso'),

]
