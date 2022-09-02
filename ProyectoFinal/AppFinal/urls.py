from django.urls import path
from .views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("cancha/", cancha, name="cancha"),
    path("jugador/", jugador, name="jugador"),
    path("score/", score, name="score"),
    path("busquedaMatricula/", busquedaMatricula, name="busquedaMatricula"),
    path("buscar/", buscar, name="buscar"),
]