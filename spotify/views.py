from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.db.models import Q

from .models import User

# Create your views here.
def home(request):
    # Render the home page
    return render(request, 'test.html') 

def login(request):
    # Render the login page
    return render(request, 'login.html')

def login_validate(request):
    if request.method == "POST":
        user_input = request.POST.get('user')
        password = request.POST.get('password')

        try:
            # Retrieve the user from the database
            user = User.objects.get(Q(user_name=user_input) | Q(email=user_input))

            # Check if the password is correct
            if check_password(password, user.password):
                # Password is correct, proceed with login
                messages.success(request, "Login successful!")
                
                return redirect('home')  # Redirect to the home page or dashboard
            else:
                messages.error(request, "Incorrect username or password.")
        except User.DoesNotExist:
            messages.error(request, "Incorrect username or password.")

    return render(request, 'login.html')  # Render login template again on error
