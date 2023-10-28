from django.shortcuts import render, redirect
from .models import Chef
from .forms import ChefForm


# Create your views here.
def Home(request):
    return render(request, "chefs/index.html")

def index_chef(request):
    chefs = Chef.objects.all()
    context = {"chefs":chefs}
    return render(request, "chefs/index_chef.html", context)

def create_chef(request):
    if request.method == "POST":
        chef_form = ChefForm(request.POST)
        if chef_form.is_valid():
            chef_form.save()
            return redirect("index")
    else:
        chef_form = ChefForm()
        context = {"chef_form": chef_form}
    return render(request, "chefs/create_chef.html", context)

def edit_chef(request, pk):
    chef = Chef.objects.filter(id = pk).first()
    chef_form = None
    error = None
    if chef:
        if request.method == "GET":
            chef_form = ChefForm(instance=chef)
        else:
            chef_form = ChefForm(request.POST, instance=chef)
            if chef_form.is_valid():
                chef_form.save()
                return redirect("index")
    else:
        error = "No existe el chef"
    context = {"chef_form": chef_form, "error": error}
    return render(request, "chefs/edit_chef.html", context)

def delete_chef(request, pk):
    chef = Chef.objects.filter(id = pk).first()
    chef.delete()
    return redirect("index_chef")
