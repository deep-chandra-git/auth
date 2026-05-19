from django.shortcuts import render, redirect
from django.http import HttpResponse
from .supabase_client import supabase
from django.contrib import messages

def home(request):
    return HttpResponse("Home Page")


def signup(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        try:

            response = supabase.auth.sign_up(
                {
                    "email": email,
                    "password": password,
                }
            )

            messages.success(request, "Account Created Successfully")

            return redirect("/login")

        except Exception as e:

            print(e)

            return render(
                request,
                "accounts/signup.html",
                {
                    "error": "Unable to create account"
                }
            )

    return render(request, "accounts/signup.html")


def login(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        try:

            response = supabase.auth.sign_in_with_password(
                {
                    "email": email,
                    "password": password
                }
            )

            request.session["user"] = response.user.email

            messages.success(request, "Login Successful")

            return redirect("/dashboard")

        except Exception as e:

            print(e)

            return render(
                request,
                "accounts/login.html",
                {
                    "error": "Invalid Email or Password"
                }
            )

    return render(request, "accounts/login.html")


def google_login(request):

    response = supabase.auth.sign_in_with_oauth(
        {
            "provider": "google",
            "options": {
                "redirect_to": "http://127.0.0.1:8000/google-callback/"
            }
        }
    )

    return redirect(response.url)

def google_callback(request):

    return HttpResponse("Google Login Successful")


def dashboard(request):

    user = request.session.get("user")

    if not user:
        return redirect("/login")

    return render(request, "accounts/dashboard.html", {
        "email": user
    })

def logout(request):

    request.session.flush()

    return redirect("/login")