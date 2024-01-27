from django.shortcuts import render, HttpResponse
from .mongo import *


def add_product_to_recipe(request):
    # создаёт рецепт или добавляет в сущ продукт
    recipe_id = request.GET['recipe_id']
    product_id = request.GET['product_id']
    weight = request.GET['weight']
    recipe_add({'recipe_id': recipe_id, 'product_id': product_id, 'weight': weight})
    return HttpResponse('Good')


def cook_recipe_v(request):
    recipe_id = request.GET['recipe_id']
    cook_recipe({'recipe_id': recipe_id})
    return HttpResponse('Good')


def show_recipes_without_product(request):
    # выводит таблицу
    product_id = request.GET['product_id']
    data = {'table': show_table({'product_id': product_id})}
    return render(request, 'main/index.html', data)