from django.db import models
from apps.base.models import Base


# Create your models here.
class Chef(Base):
    name = models.CharField("Name", max_length=30, blank=False, null=False)
    last_name = models.CharField("Last name", max_length=30, blank=False, null=False)

    class Meta:
        verbose_name = "Chef"
        verbose_name_plural = "Chefs"

    def __str__(self) -> str:
        return f"{self.name} {self.last_name}"
