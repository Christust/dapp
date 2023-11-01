from django import forms
from .models import Chef


class ChefForm(forms.ModelForm):
    class Meta:
        model = Chef
        fields = "__all__"
        labels = {"name": "Nombre del chef", "last_name": "Apellido del chef"}
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese en nombre del chef",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese en apellido del chef",
                }
            ),
        }
