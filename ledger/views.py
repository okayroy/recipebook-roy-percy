"""This file defines each view."""
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe


def index(request):
    """Define the index view."""
    return HttpResponse('Hello! This is a recipe book.')

class RecipeListView(ListView):
    """Views the recipe list."""
    model = Recipe
    template_name = 'recipes/list.html'

class RecipeDetailView(DetailView):
    """Views the details/ingredients of the recipe."""
    model = Recipe
    template_name = 'recipe/detail.html'
