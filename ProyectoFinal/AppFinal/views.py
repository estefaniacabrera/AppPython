from cmath import inf
import re
from django.http import HttpResponse
from django.shortcuts import render
from AppFinal.forms import CanchaFormulario, JugadorFormulario, ScoreFormulario
from .models import Cancha, Jugador, Score


def inicio(request):
    return render(request, "AppFinal/inicio.html")


def cancha(request):
    if request.method == "POST":
        miFormularioCancha = CanchaFormulario(request.POST)
        print(miFormularioCancha)
        if miFormularioCancha.is_valid():
            info = miFormularioCancha.cleaned_data
            print(info)
            nombreCancha = info.get("nombreCancha")
            parCancha = info.get("parCancha")
            cancha = Cancha(nombreCancha=nombreCancha, parCancha=parCancha)
            cancha.save()
            return render(request, "AppFinal/inicio.html", {"mensaje": "Cancha creada"})
        else:
            return render(request, "AppFinal/inicio.html", {"mensaje": "Error"})
    else:
        miFormularioCancha = CanchaFormulario()
        return render(
            request, "AppFinal/cancha.html", {"formulario": miFormularioCancha}
        )


def jugador(request):
    if request.method == "POST":
        miJugador = JugadorFormulario(request.POST)
        if miJugador.is_valid():
            info = miJugador.cleaned_data
            nombreJugador = info.get("nombreJugador")
            edadJugador = info.get("edadJugador")
            matriculaJugador = info.get("matriculaJugador")
            jugador = Jugador(
                nombreJugador=nombreJugador,
                edadJugador=edadJugador,
                matriculaJugador=matriculaJugador,
            )
            jugador.save()
            return render(
                request, "AppFinal/inicio.html", {"mensaje": "Jugador creado"}
            )
        else:
            return render(request, "AppFinal/inicio.html", {"mensaje": "Error"})
    else:
        miJugador = JugadorFormulario()
        return render(request, "AppFinal/jugador.html", {"formulario": miJugador})


def score(request):
    if request.method == "POST":
        miScore = ScoreFormulario(request.POST)
        if miScore.is_valid():
            info = miScore.cleaned_data
            golpesIdaScore = info.get("golpesIdaScore")
            golpesVueltaScore = info.get("golpesVueltaScore")
            golpesTotalesScore = info.get("golpesTotalesScore")
            fechaScore = info.get("fechaScore")
            score = Score(
                golpesIdaScore=golpesIdaScore,
                golpesVueltaScore=golpesVueltaScore,
                golpesTotalesScore=golpesTotalesScore,
                fechaScore=fechaScore,
            )
            score.save()
            return render(request, "AppFinal/inicio.html", {"mensaje": "Score creado"})
        else:
            return render(request, "AppFinal/inicio.html", {"mensaje": "Error"})
    else:
        miScore = ScoreFormulario()
        return render(request, "AppFinal/score.html", {"formulario": miScore})


def busquedaMatricula(request):
    return render(request, "AppFinal/busquedaMatricula.html")


def buscar(request):
    if request.GET["matriculaJugador"]:
        matri = request.GET["matriculaJugador"]
        matriculas = Jugador.objects.filter(matriculaJugador=matri)
        if len(matriculas) != 0:
            return render(
                request,
                "AppFinal/resultadoMatricula.html",
                {"matriculaJugador": matriculas},
            )
        else:
            return render(
                request,
                "AppFinal/resultadoMatricula.html",
                {"mensaje": "No hay jugador con esa matricula"},
            )
    else:
        return render(
            request, "AppFinal/busquedaMatricula.html", {"mensaje": "No enviaste datos"}
        )
