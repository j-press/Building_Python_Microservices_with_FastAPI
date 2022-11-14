from fastapi import Depends 
from model.recipes import Recipe
from repository.factory import get_recipe_repo

# Recipe Service
class RecipeService: 
    # Constructor
    def __init__(self, repo=Depends(get_recipe_repo)):
        self.repo = repo

    # Get Recipes
    def get_recipes(self):
        return self.repo.query_recipes()
    
    # Add Recipe
    def add_recipe(self, recipe: Recipe):
        self.repot.insert_recipe(recipe)