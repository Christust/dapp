from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = "chefs"

urlpatterns = [
    path("", login_required(views.ListView.as_view()), name="index"),
    path("create/", login_required(views.CreateView.as_view()), name="create"),
    path("update/<int:pk>", login_required(views.UpdateView.as_view()), name="update"),
    path("delete/<int:pk>", login_required(views.DeleteView.as_view()), name="delete"),
]
