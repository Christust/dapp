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
    template_name="chefs/edit.html"
    model=Chef
    form_class=ChefForm
    success_url=reverse_lazy("chefs:index")

class CreateView(generic.CreateView):
    template_name="chefs/create.html"
    model=Chef
    form_class=ChefForm
    success_url=reverse_lazy("chefs:index")

class DeleteView(generic.DeleteView):
    model=Chef
    success_url=reverse_lazy("chefs:index")

def create(request):
    if request.method == "POST":
        chef_form = ChefForm(request.POST)
        if chef_form.is_valid():
            chef_form.save()
            return redirect("chefs:index")
    else:
        chef_form = ChefForm()
        context = {"chef_form": chef_form}
    return render(request, "chefs/create.html", context)


def update(request, pk):
    chef = Chef.objects.filter(id=pk).first()
    chef_form = None
    error = None
    if chef:
        if request.method == "GET":
            chef_form = ChefForm(instance=chef)
        else:
            chef_form = ChefForm(request.POST, instance=chef)
            if chef_form.is_valid():
                chef_form.save()
                return redirect("chefs:index")
    else:
        error = "No existe el chef"
    context = {"chef_form": chef_form, "error": error}
    return render(request, "chefs/edit.html", context)


def show(request, pk):
    chef = Chef.objects.filter(id=pk).first()
    chef_form = None
    error = None
    if chef:
        chef_form = ChefForm(instance=chef)
    else:
        error = "No existe el chef"
    context = {"chef_form": chef_form, "error": error}
    return render(request, "chefs/edit.html", context)


def delete(request, pk):
    chef = Chef.objects.filter(id=pk).first()
    chef.delete()
    return redirect("chefs:index")
