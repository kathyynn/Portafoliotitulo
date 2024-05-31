from django import forms
from .models import Encuesta

class EncuestaForm(forms.ModelForm):
    calificacion = forms.IntegerField(
        label='Calificación (del 1 al 7)',
        min_value=1,
        max_value=7,
        widget=forms.NumberInput(attrs={'type': 'number', 'min': '1', 'max': '7'})
    )

    class Meta:
        model = Encuesta
        fields = ['texto_encuesta', 'activa']