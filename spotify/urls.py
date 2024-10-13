from django.urls import path
from spotify import views

urlpatterns = [
    path("", views.login, name='login'),
    path("home", views.home, name='home'),
    path("login_validate", views.login_validate, name="login_validate"),
    path("sign_up", views.sign_up, name="sign_up"),
    path("sign_up_email", views.sign_up_email, name="sign_up_email"),
    path("sign_up_form", views.sign_up_form, name="sign_up_form"),
    path("reset_password", views.reset_password, name="reset_password"),
    path("reset_password_submission", views.reset_password_submission, name="reset_password_submission"),
]