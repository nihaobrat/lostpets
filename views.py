from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from models import Animal, User
from forms import UserForm, AnimalForm


@login_required(login_url="login/")
def index(request):
    animals = Animal.objects.all()
    return render(request, "index.html", {"animals": animals})


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = UserForm()

    return render(request, "register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "login.html", {"error_message": "Неправильный логин или пароль."})
    else:
        return render(request, "login.html")


def user_logout(request):
    logout(request)
    return redirect("index")
