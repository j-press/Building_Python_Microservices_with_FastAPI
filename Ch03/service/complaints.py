from fastapi import Depends
from repository.factory import get_bad_recipes
from uuid import UUID 

# Bad Recipe Service
class BadRecipeService: 

    # Constructor 
    def __init__(self, recipes=Depends(get_bad_recipes)):
        self.recipes = recipes 

    # Report bad recipe
    def report_bad_recipe(self, id: UUID):
        self.recipes.add_bad_recipe(id)
    
    # Get bad recipes
    def get_bad_recipes(self):
        return self.recipes.query_bad_recipes()