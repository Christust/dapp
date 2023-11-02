from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"
        labels = {
            "name": "Nombre de la receta",
            "description": "Descripción",
            "chef": "Chef de la receta",
        }
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese en nombre de la receta",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese una descripción",
                }
            ),
            "chef": forms.Select(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese en nombre del chef",
                }
            ),
        }
