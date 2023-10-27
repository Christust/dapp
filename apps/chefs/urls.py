from django.urls import path
from .views import Home, create_chef

urlpatterns = [
    path("", Home, name="index"),
    path("create_chef/", create_chef, name="create_chef")
]
