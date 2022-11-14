from fastapi import Depends
from service.recipes import RecipeService
from service.posts import PostService 
from service.complaints import BadRecipeService

# Get Recipe Service
def get_recipe_service(repo=Depends(RecipeService)):
    return repo

# Get Post Service
def get_post_service(repo=Depends(PostService)):
    return repo

# Get Complaint Service
def get_complaint_service(repo=Depends(BadRecipeService)):
    return repo
