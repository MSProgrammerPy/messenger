from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from .models import User


# Create your views here.


def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")

    login_form = LoginForm(request.POST or None)

    context = {
        "login_form": login_form
    }

    if login_form.is_valid():
        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            context["login_form"] = LoginForm()
            return redirect("/")
        else:
            login_form.add_error("password", _("Incorrect username or password."))

    return render(request, "auth/login.html", context)


def register_page(request):
    if request.user.is_authenticated:
        return redirect("/")

    register_form = RegisterForm(request.POST or None, request.FILES or None)

    context = {
        "register_form": register_form
    }

    if register_form.is_valid():
        username = register_form.cleaned_data.get("username")
        password = register_form.cleaned_data.get("password")
        picture = register_form.cleaned_data.get("picture")

        user = User.objects.create_user(username=username, password=password, picture=picture)

        login(request, user)
        context["register_form"] = RegisterForm()
        return redirect("/")

    return render(request, "auth/register.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")
