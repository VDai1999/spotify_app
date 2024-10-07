from django.urls import path
from spotify import views

urlpatterns = [
    path("", views.login, name='login'),
    path("home", views.home, name='home'),
    path("login_validate", views.login_validate, name="login_validate")
]