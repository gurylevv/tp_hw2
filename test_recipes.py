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


# Тестирование класса ShoppingList
#-----------------------------------

def test_add_recipe():
    recipe = Recipe("Пицца")
    recipe.add_ingredient(Ingredient("Мука",100,"г"))
    shopping = ShoppingList()
    shopping.add_recipe(recipe,2)
    assert len(shopping._items) == 1

def test_add_recipe_error():
    shopping = ShoppingList()
    recipe = Recipe("Пицца")
    with pytest.raises(ValueError):
        shopping.add_recipe(recipe,0)

def test_remove_recipe():
    recipe = Recipe("Пицца")
    recipe.add_ingredient(Ingredient("Мука",100,"г"))
    shopping = ShoppingList()
    shopping.add_recipe(recipe,1)
    shopping.remove_recipe("Пицца")
    assert len(shopping._items) == 0


def test_get_list():
    r1 = Recipe("A")
    r2 = Recipe("B")
    r1.add_ingredient(Ingredient("Мука",100,"г"))
    r2.add_ingredient(Ingredient("Мука",50,"г"))
    shopping = ShoppingList()
    shopping.add_recipe(r1, 1)
    shopping.add_recipe(r2, 1)
    result = shopping.get_list()
    assert result[0].quantity == 150


def test_shopping_list_add():
    sl1 = ShoppingList()
    r1 = Recipe("Рецепт 1")
    r1.add_ingredient(Ingredient("Мука", 100, "г"))
    sl1.add_recipe(r1, 1)
    sl2 = ShoppingList()
    r2 = Recipe("Рецепт 2")
    r2.add_ingredient(Ingredient("Сахар", 50, "г"))
    sl2.add_recipe(r2, 1)
    sl3 = sl1 + sl2
    assert len(sl3.get_list()) == 2
    assert len(sl1.get_list()) == 1
    assert len(sl2.get_list()) == 1