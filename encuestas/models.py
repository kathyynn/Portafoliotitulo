from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

class Encuesta(models.Model):
    id_encuesta = models.AutoField(primary_key=True)
    texto_encuesta = models.CharField(max_length=200)
    activa = models.BooleanField(default=False)

    def __str__(self):
        return self.texto_encuesta

class ResultadoEncuesta(models.Model):
    encuesta = models.ForeignKey('Encuesta', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    calificacion = models.IntegerField(choices=[(i, i) for i in range(1, 8)])

    def __str__(self):
        return f"Encuesta: {self.encuesta.texto_encuesta}, Usuario: {self.usuario.username}, Calificación: {self.calificacion}"
    

def calcular_promedio_encuesta(encuesta):
    promedio = ResultadoEncuesta.objects.filter(encuesta=encuesta).aggregate(promedio=Avg('calificacion'))['promedio']
    return promedio