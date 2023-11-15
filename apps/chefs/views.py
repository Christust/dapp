from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Chef
from .forms import ChefForm


# Create your views here.
class ListView(generic.ListView):
    template_name = "chefs/index.html"
    context_object_name = "chefs"
    model = Chef
    queryset = model.objects.all()

class UpdateView(generic.UpdateView):
    template_name = "chefs/edit.html"
    model = Chef
    form_class = ChefForm
    success_url = reverse_lazy("chefs:index")


class CreateView(generic.CreateView):
    template_name = "chefs/create.html"
    model = Chef
    form_class = ChefForm
    success_url = reverse_lazy("chefs:index")


class DeleteView(generic.DeleteView):
    model = Chef
    success_url = reverse_lazy("chefs:index")
