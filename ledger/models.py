"""This file provides the base models for python."""

from django.db import models
from django.urls import reverse


class Ingredient(models.Model):
    """This class represents the ingredients in a recipe."""

    name = models.CharField(max_length=100)

    def __str__(self):
    """Returns name of the ingredient."""

        return self.name
    
    def get_absolute_url(self):
    """Returns absolute url of the ingredients."""

        return reverse('ingredient_detail', args=[str(self.name)])


class Recipe(models.Model):
    """This class represents the recipes itself."""

    name = models.CharField(max_length=100)

    def __str__(self):
    """Returns recipe name."""

        return self.name
    
    def get_absolute_url(self):
    """Returns absolute url of the recipe."""

        return reverse('recipe_detail', args=[str(self.name)])


class RecipeIngredient(models.Model):
    """This class specifies quantity, and uses foreign keys to refer
    back to previously established recipes and ingredients."""
    
    quantity = models.CharField(max_length=100)
    
    ingredient - models.ForeignKey(
        Ingredient,
        on_delete=models.SET_NULL,
        null=True,
        related_name='recipe',
    )
    
    recipe - models.ForeignKey(
        Recipe,
        on_delete=models.SET_NULL,
        null=True,
        related_name='ingredients',
    )