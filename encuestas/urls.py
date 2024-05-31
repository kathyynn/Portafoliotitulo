from django.urls import path
from .views import crear_encuesta, ver_encuestas, guardar_encuesta

urlpatterns = [
    path('crear/', crear_encuesta, name='crear_encuesta'),
    path('ver/', ver_encuestas, name='ver_encuestas'),
    path('guardar/', guardar_encuesta, name='guardar_encuesta'),
]
