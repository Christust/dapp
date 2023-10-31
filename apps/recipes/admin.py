from django.contrib import admin
from .models import Recipe


# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "chef"]


admin.site.register(Recipe, RecipeAdmin)
