from django.shortcuts import render, redirect
from .forms import EncuestaForm
from .models import Encuesta


def crear_encuesta(request):
    if request.method == 'POST':
        form = EncuestaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_encuestas')
    else:
        form = EncuestaForm()
    return render(request, 'crear_encuesta.html', {'form': form})


def ver_encuestas(request):
    encuestas = Encuesta.objects.all()
    return render(request, 'ver_encuestas.html', {'encuestas': encuestas})


def guardar_encuesta(request):
    # Aquí manejas la lógica para guardar la encuesta
    if request.method == 'POST':
        form = EncuestaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_encuestas')  # Redirecciona a la página de ver encuestas después de guardar
    else:
        form = EncuestaForm()
    return render(request, 'crear_encuesta.html', {'form': form})  # Puedes renderizar la misma página de creación de encuesta con el formulario y mostrar errores si es necesario
