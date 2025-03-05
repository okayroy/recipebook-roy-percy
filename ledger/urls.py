"""This file defines the url path for each view."""
from django.urls import path
from .views import index, RecipeListView, RecipeDetailView


urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:id>', RecipeDetailView.as_view(), name='recipe-detail'),
    ]

app_name = "ledger"
