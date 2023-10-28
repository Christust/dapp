from django.db import models
from apps.chefs.models import Chef


# Create your models here.
class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Name", max_length=30, blank=False, null=False)
    description = models.TextField(
        "Description", blank=False, null=False
    )
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"

    def __str__(self) -> str:
        return self.name
