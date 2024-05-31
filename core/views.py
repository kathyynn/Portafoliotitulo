from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import UserRegistrationForm

# Create your views here.


def productos(request):
    return render(request, "productos.html")


def signup(request):
    if request.method == "POST":

        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            messages.add_message(request=request,level=messages.SUCCESS, message="Usuario registrado")
            return redirect("signup")
        else:
             messages.add_message(request=request,level=messages.WARNING, message="Error al registrar")
    else:
        form = UserRegistrationForm()

    context = {"form": form}

    return render(request, "signup.html", context)
