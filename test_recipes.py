import pytest
from recipes import Ingredient, Recipe, ShoppingList, DietaryRecipe

# Тестирование класса Ingredient
#--------------------------------------
def test_ingredient_creation():
    ing = Ingredient("Мука", 500, "г")
    assert ing.name == "Мука"
    assert ing.quantity == 500.0
    assert ing.unit == "г"

def test_ingredient_str():
    ing = Ingredient("Сахар", 100, "г")
    assert str(ing) == "Сахар: 100.0 г"

def test_ingredient_eq():
    ing1 = Ingredient("Яйцо", 2, "шт")
    ing2 = Ingredient("Яйцо", 5, "шт")
    ing3 = Ingredient("Молоко", 2, "шт")
    ing4 = Ingredient("Яйцо", 2, "кг")
    assert ing1 == ing2 
    assert ing1 != ing3
    assert ing1 != ing4

def test_ingredient_neg_quantity():
    with pytest.raises(ValueError, match="Количество должно быть положительным"):
        Ingredient("Мука", -10, "г")


# Тестирование класса Recipe
#---------------------------

def test_recipe_creation():
    recipe = Recipe("Пицца")
    assert recipe.title == "Пицца"
    assert recipe.ingredients == []

def test_add_ingredient():
    recipe = Recipe("Пицца")
    recipe.add_ingredient(Ingredient("Мука",500,"г"))
    assert len(recipe) == 1

def test_merge_ingredients():
    recipe = Recipe("Пицца")
    recipe.add_ingredient(
        Ingredient("Мука",500,"г"))
    recipe.add_ingredient(Ingredient("Мука",200,"г"))
    assert len(recipe) == 1
    assert (recipe.ingredients[0].quantity==700)

def test_scale():
    recipe = Recipe("Пицца")
    recipe.add_ingredient(
        Ingredient("Мука",100,"г"))

    scaled = recipe.scale(2)
    assert scaled is not recipe
    assert (scaled.ingredients[0].quantity == 200)

def test_scale_error():
    recipe = Recipe("Пицца")
    with pytest.raises(ValueError):
        recipe.scale(0)