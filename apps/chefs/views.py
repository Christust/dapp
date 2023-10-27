from django.shortcuts import render, redirect
from .forms import ChefForm


# Create your views here.
def Home(request):
    return render(request, "chefs/index.html")


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
