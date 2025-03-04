"""This file defines the url path for each view"""

from django.urls import path
from .views import index, recipes_view, recipe1_view, recipe2_view


urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', recipes_view, name='recipelist'),
    path('recipe/1', recipe1_view, name="recipe1"),
    path('recipe/2', recipe2_view, name="recipe2")
    ]

app_name = "ledger"
