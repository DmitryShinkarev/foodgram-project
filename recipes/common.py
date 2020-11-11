from decimal import Decimal
from django.db import IntegrityError, transaction


from .models import Ingredient, IngredientAmount, Recipe, Tag


def filter_tag(request):
    '''Функция готовит общую выборку рецептов в зависимости от тега
    для дальнейшего фильтрования при необходимости.'''
    tags = request.GET.get('tags', 'bds')
    recipe_list = Recipe.objects.prefetch_related(
        'author', 'recipe_tag'
            ).filter(
        recipe_tag__slug__in=tags
            ).distinct()
    return recipe_list, tags


def get_tag(tags):
    '''Функция переводит русские названия в английские. Нужна для
    корректного отображения тегов при создании и редактировании рецепта.'''
    tag_dict = {
        'Завтрак': 'breakfast',
        'Обед': 'lunch',
        'Ужин': 'dinner',
    }
    return [tag_dict[item] for item in tags]


def save_recipe(request, form):
    '''Функция сохраняет данные в db при создании и редактировании рецепта.'''
    try:
        with transaction.atomic():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()

            tags = form.cleaned_data['tag']
            for tag in tags:
                Tag.objects.create(recipe=recipe, title=tag)

            objs = []
            for key, value in form.data.items():
                if 'nameIngredient' in key:
                    title = value
                elif 'valueIngredient' in key:
                    amount = Decimal(value.replace(',', '.'))
                elif 'unitsIngredient' in key:
                    dimension = value
                    ing = Ingredient.objects.get(title=title, dimension=dimension)
                    objs.append(
                        IngredientAmount(ingredient=ing, recipe=recipe, amount=amount)
                    )
            IngredientAmount.objects.bulk_create(objs)
            return None
    except IntegrityError:
        return 400
