from django import forms


class CanchaFormulario(forms.Form):
    nombreCancha = forms.CharField(max_length=80)
    parCancha = forms.IntegerField()


class JugadorFormulario(forms.Form):
    nombreJugador = forms.CharField(max_length=80)
    edadJugador = forms.CharField(max_length=80)
    matriculaJugador = forms.IntegerField()


class ScoreFormulario(forms.Form):
    golpesIdaScore = forms.IntegerField()
    golpesVueltaScore = forms.IntegerField()
    golpesTotalesScore = forms.IntegerField()
    fechaScore = forms.DateField()