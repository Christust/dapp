from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Chef
from .forms import ChefForm


# Create your views here.
class ListView(generic.View):
    template_name = "chefs/index.html"
    context_object_name = "chefs"
    model = Chef
    form_class = ChefForm
    queryset = model.objects.all()

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = {"chefs": self.get_queryset(), "form": self.form_class}
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = self.form_class(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect("chefs:index")


class UpdateView(generic.UpdateView):
    template_name = "chefs/edit_chef_modal.html"
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
