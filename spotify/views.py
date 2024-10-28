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
from django.conf import settings
from django.http import JsonResponse


from urllib.parse import urlencode
from dotenv import load_dotenv
from openai import OpenAI
import os

from .models import User

# Load keys from .env file
load_dotenv() 

openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(
  api_key=openai_api_key,
)


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
                
                return redirect('home')  # Redirect to the home page
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
        # next_url = reverse('sign_up_form')
        # query_string = urlencode({'email': email})  # Create query string
        # return HttpResponseRedirect(f'{next_url}?{query_string}')
        request.session['email'] = email
        
        # Redirect to the form to sign up
        return redirect("sign_up_form")

    return render(request, 'signup.html')

def sign_up_form(request):
    # email = request.GET.get('email', None)
    # Retrieve the email from the session
    email = request.session.get('email')

    if email is None:
        # If the email is not found, redirect back to the signup page
        messages.error(request, "Session expired or email not provided.")
        return redirect('sign_up')

    # Render the signup password page
    return render(request, 'signup_form.html', {'email': email})

def save_sign_up(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        display_name = request.POST.get('name')
        birth_date = request.POST.get('birthdate')
        gender = request.POST.get('gender')

        new_user = User(
            email=email,
            password=password,
            display_name=display_name,
            date_of_birth=birth_date,
            gender=gender
        )
        new_user.save()

        messages.success(request, "Account created successfully!")
        return redirect('login')  # Replace with your login URL

    return render(request, 'signup.html')  # Render sign-up form if GET request

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

def dashboard(request):
    return render(request, 'dashboard.html')

def chatbot(request):
    return render(request, 'chatbot.html')

def get_openai_answer(request):
    if request.method == "POST":
        prompt = request.POST.get("userInput")

        try:
            response = client.chat.completions.create(
                model = "gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                stream=False,
                max_tokens = 1024,
            )

            # Retrieve the response text
            answer = response.choices[0].message.content

            return JsonResponse({"completion": answer})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return render(request, "chatbot.html")
    
def download_app(request):
    return render(request, 'download_app.html')

def notification(request):
    return render(request, 'notification.html')

