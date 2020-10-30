from django.urls import path
from .views import Inicio,Listado

urlpatterns = [
    path('',Inicio.as_view(), name = 'index'),
    path('videojuegos/',Listado.as_view(),{'nombre_categoria':'Videojuegos'}, name = 'videojuegos'),
    path('generales/',Listado.as_view(),{'nombre_categoria':'General'}, name = 'generales'),
]