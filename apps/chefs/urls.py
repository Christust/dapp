from django.urls import path
from . import views

app_name='chefs'

urlpatterns = [
    path("", views.Home, name="index"),
    path("create_chef/", views.create_chef, name="create_chef"),
    path("index_chef/", views.index_chef, name="index_chef"),
    path("edit_chef/<int:pk>", views.edit_chef, name="edit_chef"),
    path("delete_chef/<int:pk>", views.delete_chef, name="delete_chef"),
]
