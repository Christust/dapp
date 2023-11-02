from django.urls import path
from django.contrib.auth.views import logout_then_login
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.Login.as_view(template_name="login.html"), name="login"),
    path("logout/", logout_then_login, name="logout"),
]
