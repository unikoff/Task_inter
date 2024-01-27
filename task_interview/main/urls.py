from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_product_to_recipe),
    path('cook_recipe/', views.cook_recipe_v),
    path('show_tables/', views.show_recipes_without_product)
]