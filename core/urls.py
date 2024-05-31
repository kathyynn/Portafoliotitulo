from django.urls import path
from .views import signup, productos

urlpatterns = [
    path('', signup, name="signup"),
    path('productos',productos,name="productos")
]