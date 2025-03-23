from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature  # Import the Feature model

def index(request):
    # Fetch all Feature objects from the database
    features = Feature.objects.all()

    # Pass the features to the template
    context = {
        "features": features,
    }

    return render(request, "index.html", context)

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Used")
                return redirect("register")  # Redirect to the same page if email exists
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Exists")
                return redirect("register")  # Redirect to the same page if username exists
            else:
                # Create the user and redirect to the login page
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Registration successful! Please log in.")
                return redirect("login")  # Redirect to the login page after successful registration
        else:
            messages.info(request, "Passwords Do Not Match")
            return redirect("register")  # Redirect to the same page if passwords don't match
    else:
        # Render the registration form for GET requests
        return render(request, "register.html")

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")  # Redirect to the home page after login
        else:
            messages.info(request, "Invalid Credentials")
            return redirect("login")  # Redirect to the same page if login fails
    else:
        return render(request, "login.html")