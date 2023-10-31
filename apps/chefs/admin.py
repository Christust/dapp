from django.contrib import admin
from .models import Chef


# Register your models here.
class ChefAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display=["name", "last_name"]


admin.site.register(Chef, ChefAdmin)
