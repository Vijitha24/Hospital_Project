from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from Userauthapp import forms as Userauthapp_forms
from doctor import models as doctor_models
from patient import models as patient_models
from Userauthapp import models as Userauthapp_models


def register_view(request):
    if request.user.is_authenticated:
        messages.success(request, "You are already logged in")
        return redirect("/")

    if request.method == "POST":
        form = Userauthapp_forms.UserRegisterForm(request.POST or None)

        if form.is_valid():
            user = form.save()
            full_name = form.cleaned_data.get("full_name")
            email = form.cleaned_data.get("email")
            password1 = form.cleaned_data.get("password1")
            user_type = form.cleaned_data.get("user_type")

            user = authenticate(request, email=email, password=password1)
            print("user ========= ", user)

            if user is not None:
                login(request, user)

                if user_type == "Doctor":
                    doctor_models.Doctor.objects.create(user=user, full_name=full_name)
                else:
                    patient_models.Patient.objects.create(user=user, full_name=full_name, email=email)

                messages.success(request, "Account created successfully")
                return redirect("/")

            else:
                messages.error(request, "Authenticated failed, please try again!")

    else:
        form = Userauthapp_forms.UserRegisterForm()

    context = {
        "form": form
    }
    return render(request, "userauths/sign_up.html", context)


def login_view(request):
    if request.user.is_authenticated:
        messages.success(request, "You are already logged in")
        return redirect("/")

    if request.method == "POST":
        form = Userauthapp_forms.LoginForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            # Authenticate user with email and password
            user_authenticate = authenticate(request, email=email, password=password)

            if user_authenticate is not None:
                login(request, user_authenticate)
                messages.success(request, "Login successful")

                next_url = request.GET.get("next", '/')
                return redirect(next_url)
            else:
                messages.error(request, "Invalid email or password!")

    else:
        form = Userauthapp_forms.LoginForm()

    context = {
        "form": form
    }
    return render(request, "userauths/sign_in.html", context)

def logout_view(request):
    logout(request)
    messages.success(request, "Logout successful")
    return redirect("Userauthapp:sign_in")