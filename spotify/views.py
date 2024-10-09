from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.db.models import Q
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect

from urllib.parse import urlencode

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

def sign_up(request):
    # Render the home page
    return render(request, 'signup.html') 

def sign_up_email(request):    
    if request.method == "POST":
        email = request.POST.get('email')

        # Validate the email
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "This email is invalid. Make sure it's written like example@email.com")
            return render(request, 'signup.html')  # Render the signup page again with the error message
        
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            # If email exists, create a warning message and redirect to the login page
            login_url = reverse('login')  # Ensure 'login' is the correct URL name
            login_link = mark_safe(f"This address is already linked to an existing account. To continue, <a href='{login_url}'>log in</a>.")
            messages.warning(request, login_link)
            return render(request, 'signup.html')  # Render the signup page again with the warning message
        
        # If email is valid and doesn't exist, redirect to the next step (password signup) and pass the email
        next_url = reverse('sign_up_password')
        query_string = urlencode({'email': email})  # Create query string
        return HttpResponseRedirect(f'{next_url}?{query_string}')

    # If GET request, render the signup form
    return render(request, 'signup.html')

def sign_up_password(request):
    email = request.GET.get('email', None)

    # Render the signup password page
    return render(request, 'signup_password.html', {'email': email})

def reset_password(request):
    # Render the signup password page
    return render(request, 'reset_password.html')

def reset_password_submission(request):
    if request.method == "POST":
        user_input = request.POST.get('user')
        password = request.POST.get('password')

        try:
            # Retrieve the user from the database using username or email
            user = User.objects.get(Q(user_name=user_input) | Q(email=user_input))
            
            # Hash the password before saving it (important for security)
            user.password = make_password(password)  # Hash password using Django's utility
            user.save()

            # Provide feedback to the user
            messages.success(request, "Password has been successfully reset.")
            return redirect('login')  # Redirect to login page or any other page

        except User.DoesNotExist:
            messages.error(request, "Incorrect email address or username.")
    
    # If form submission fails, stay on the same page with the error message
    return render(request, 'reset_password.html')