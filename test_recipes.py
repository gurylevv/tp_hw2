import pytest
from recipes import Ingredient, Recipe, ShoppingList, DietaryRecipe


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