from django.urls import reverse_lazy
from django.views import generic
from .models import Recipe
from .forms import RecipeForm


# Create your views here.
class ListView(generic.ListView):
    template_name = "recipes/index.html"
    context_object_name = "recipes"
    model = Recipe
    queryset = model.objects.all()


class UpdateView(generic.UpdateView):
    template_name = "recipes/edit.html"
    model = Recipe
    form_class = RecipeForm
    success_url = reverse_lazy("recipes:index")


class CreateView(generic.CreateView):
    template_name = "recipes/create.html"
    model = Recipe
    form_class = RecipeForm
    success_url = reverse_lazy("recipes:index")

class ShowView(generic.UpdateView):
    template_name = "recipes/show.html"
    model = Recipe
    form_class = RecipeForm
    success_url = reverse_lazy("recipes:index")


class DeleteView(generic.DeleteView):
    model = Recipe
    success_url = reverse_lazy("recipes:index")
