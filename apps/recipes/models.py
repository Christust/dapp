from django.db import models
from apps.base.models import Base
from apps.chefs.models import Chef


# Create your models here.
class Recipe(Base):
    name = models.CharField("Name", max_length=30, blank=False, null=False)
    description = models.TextField(
        "Description", blank=False, null=False
    )
    instructions = models.TextField(
        "Instructions", blank=False, null=False
    )
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"

    def __str__(self) -> str:
        return self.name
