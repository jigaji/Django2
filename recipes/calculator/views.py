from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'charlotte': {
        'яйцо, шт': 4,
        'сахар, г': 100,
        'мука, г': 100,
        'яблоки, шт': 4,
        'разрыхлитель, ч.л.': 1
    },
    'ramyon': {
        'рамён, пачка': 1,
        'вода, мл': 400,
        'сыр, ломтик': 1,
        'сосиска, шт': 1,
        'яйцо, шт': 1,
    },
}

    # можете добавить свои рецепты ;)

def get_recipe(request, recipe_name):
    if recipe_name in DATA:
        recipe = DATA[recipe_name]
        servings = int(request.GET.get("servings", 1))
        if servings:
            ingridients = dict()
            for ingridient, amount in recipe.items():
                count_amount = amount * servings
                ingridients[ingridient] = count_amount
            context = {
                'recipe_name': recipe_name,
                'recipe': ingridients,
            }
        else:
            context = {
                'recipe_name': recipe_name,
                'recipe': recipe,
            }


        return render(request, 'calculator/index.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
