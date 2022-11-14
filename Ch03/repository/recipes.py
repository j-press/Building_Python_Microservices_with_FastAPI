# Import models from recipes.py
from model.recipes import Recipe, Ingredient
# Import models from classifications.py 
from model.classifications import Category, Origin
# Import uuid4 from uuid
from uuid import uuid4

recipes = dict()

class RecipeRepository: 
    def __init__(self):
        ingrA1 = Ingredient(measure='cup', qty=1, name='grape tomatoes', id=uuid4())
        ingrA2 = Ingredient(measure='cup', qty=1, name='red onion', id=uuid4())
        ingrA3 = Ingredient(measure='cup', qty=1, name='feta cheese', id=uuid4())
        ingrA4 = Ingredient(measure='cup', qty=1, name='kalamata olives', id=uuid4())
        ingrA5 = Ingredient(measure='cup', qty=1, name='fresh basil', id=uuid4())
        ingrA6 = Ingredient(measure='cup', qty=1, name='extra virgin olive oil', id=uuid4())
        ingrA7 = Ingredient(measure='cup', qty=1, name='balsamic vinegar', id=uuid4())
        ingrA8 = Ingredient(measure='cup', qty=1, name='salt', id=uuid4())
        ingrA9 = Ingredient(measure='cup', qty=1, name='pepper', id=uuid4())

        recipeA = Recipe(origin=Origin.european, ingredient=[ingrA1, ingrA2, ingrA3, ingrA4, ingrA5, ingrA6, ingrA7, ingrA8, ingrA9], category=Category.breakfast, name='Crutless quiche bites with fresh basil and extra virgin olive oil', id=uuid4())

        ingrB1 = Ingredient(measure='tablespoon', qty=1, name='oil', id=uuid4())
        ingrB2 = Ingredient(measure='cup', qty=1, name='onion', id=uuid4())
        ingrB3 = Ingredient(measure='cup', qty=1, name='garlic', id=uuid4())
        ingrB4 = Ingredient(measure='cup', qty=1, name='chicken broth', id=uuid4())
        ingrB5 = Ingredient(measure='cup', qty=1, name='tomato sauce', id=uuid4())
        ingrB6 = Ingredient(measure='cup', qty=1, name='tomato paste', id=uuid4())
        ingrB7 = Ingredient(measure='cup', qty=1, name='dried oregano', id=uuid4())
        ingrB8 = Ingredient(measure='cup', qty=1, name='dried basil', id=uuid4())
        ingrB9 = Ingredient(measure='cup', qty=1, name='salt', id=uuid4())

        recipeB = Recipe(origin=Origin.european, ingredient=[ingrB1, ingrB2, ingrB3, ingrB4, ingrB5, ingrB6, ingrB7, ingrB8, ingrB9], category=Category.breakfast, name='Easy homemade spaghetti sauce', id=uuid4())

        ingrC1 = Ingredient(measure='pounds', qty=2.25, name='sweet yellow onions', id=uuid4())
        ingrC2 = Ingredient(measure='cloves', qty=10, name='garlic', id=uuid4())
        ingrC3 = Ingredient(measure='minced', qty=1, name='black pepper', id=uuid4())
        ingrC4 = Ingredient(measure='drop', qty=1, name='kasher salt', id=uuid4())
        ingrC5 = Ingredient(measure='cup', qty=4, name='low-sodium chicken brothlarge eggs', id=uuid4())
        ingrC6 = Ingredient(measure='tablespoon', qty=4, name='sherry', id=uuid4())
        ingrC7 = Ingredient(measure='sprig', qty=7, name='thyme', id=uuid4())
        ingrC8 = Ingredient(measure='cup', qty=0.5, name='heavy cream', id=uuid4())
    

        recipeC = Recipe(origin=Origin.mediterranean, ingredient=[ingrC1, ingrC2, ingrC3, ingrC4, ingrC5, ingrC6, ingrC7, ingrC8], category=Category.soup, name='Creamy roasted onion soup', id=uuid4())

        recipes[recipeA.id] = recipeA
        recipes[recipeB.id] = recipeB
        recipes[recipeC.id] = recipeC

def insert_recipe(self, recipe: Recipe):
    recipes[recipe.id] = recipe 

def query_recipes(self):
    return recipes