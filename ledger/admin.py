"""This file sets up the admin panel."""
from django.contrib import admin
from .models import Recipe, RecipeIngredient


class RecipeInLine(admin.TabularInLine):
    """Creates InlineAdmin of RecipeIngredient."""

    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    """Admin panel for the Recipe model."""

    inlines = [RecipeInLine, ]
    model = Recipe
    search_fields = ('name', )


admin.site.register(Recipe, RecipeAdmin)
