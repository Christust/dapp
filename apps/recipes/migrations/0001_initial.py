# Generated by Django 4.2.6 on 2023-11-19 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("chefs", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Recipe",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("is_active", models.BooleanField(default=True, verbose_name="Status")),
                (
                    "created_at",
                    models.DateField(auto_now_add=True, verbose_name="Creation date"),
                ),
                (
                    "modified_at",
                    models.DateField(auto_now=True, verbose_name="Modification date"),
                ),
                (
                    "deleted_at",
                    models.DateField(
                        blank=True, null=True, verbose_name="Deletion date"
                    ),
                ),
                ("name", models.CharField(max_length=30, verbose_name="Name")),
                ("description", models.TextField(verbose_name="Description")),
                ("instructions", models.TextField(verbose_name="Instructions")),
                (
                    "chef",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="chefs.chef"
                    ),
                ),
            ],
            options={
                "verbose_name": "Recipe",
                "verbose_name_plural": "Recipes",
            },
        ),
    ]
