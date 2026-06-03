class Ingredient:

    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = float(value)

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"
    
    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"
    
    def __eq__(self, other):
        return self.name == other.name and self.unit == other.unit


class Recipe:

    def __init__(self, title, ingredients=None):
        self.title = title
        if ingredients is None:
            ingredients = []
        self.ingredients = ingredients

    def add_ingredient(self, ingredient):
        for e in self.ingredients:
            if e == ingredient:
                e.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        return isinstance(ratio, (int, float)) and ratio > 0
    
    def scale(self, ratio):
        if not self.is_valid_ratio(ratio):
            raise ValueError("Коэффициент должен быть положительным")
        new_ingredients = []
        for ing in self.ingredients:
            new_ingredients.append(Ingredient(ing.name, ing.quantity * ratio, ing.unit))
        return Recipe(self.title, new_ingredients)

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        text = f"{self.title}\n"
        for ing in self.ingredients:
            text += str(ing) + "\n"
        return text
    

class ShoppingList:

    def __init__(self):
        self._items = []

    def add_recipe(self, recipe, portions):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        scaled = recipe.scale(portions)
        for ingredient in scaled.ingredients:
            self._items.append((ingredient, recipe.title))

    def remove_recipe(self, title):
        new_items = []
        for ingredient, recipe_title in self._items:
            if recipe_title != title:
                new_items.append((ingredient, recipe_title))
        self._items = new_items
    
    def get_list(self):
        totals = {}
        for ingredient, recipe_title in self._items:
            key = (ingredient.name, ingredient.unit)
            if key in totals:
                totals[key] += ingredient.quantity
            else:
                totals[key] = ingredient.quantity
        result = []
        for (name, unit), quantity in totals.items():
            result.append(Ingredient(name, quantity, unit))
        result.sort(key=lambda ing: ing.name)
        return result
    
    def __add__(self, other):
        lst = ShoppingList()
        lst._items = self._items + other._items
        return lst