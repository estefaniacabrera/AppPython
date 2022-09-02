from django.db import models


class Cancha(models.Model):
    nombreCancha = models.CharField(max_length=60)
    parCancha = models.IntegerField()


class Jugador(models.Model):
    nombreJugador = models.CharField(max_length=60)
    edadJugador = models.CharField(max_length=60)
    matriculaJugador = models.IntegerField()


class Score(models.Model):
    golpesIdaScore = models.IntegerField()
    golpesVueltaScore = models.IntegerField()
    golpesTotalesScore = models.IntegerField()
    fechaScore = models.DateField()