from uuid import UUID 
from repository.recipes import recipes

# Recipe Dictionary
recipe_bad = dict()

# Recipe Repository
class BadRecipeRepository: 
    def __init__(self):
        pass 

    # Add Bad Recipe
    def add_bad_recipe(self, id: UUID):
        recipe_bad[id] = id 

    # Get Bad Recipes
    def query_bad_recipe(self):
        return list(recipe_bad.values())