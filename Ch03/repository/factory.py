from fastapi import Depends
from repository.recipes import RecipeRepository
from repository.posts import PostRepository
from repository.admin import AdminRepository
from repository.keywords import KeywordRepository
from repository.complaints import BadRecipeRepository

# Get Recipe Repository
def get_recipe_repo(repo=Depends(RecipeRepository)):
    return repo

# Get Post Repository
def get_post_repo(repo=Depends(PostRepository)):
    return repo

# Get User Repository
def get_users_repo(repo=Depends(AdminRepository)):
    return repo

# Get Keyword Repository
def get_keywords(repo=Depends(KeywordRepository)):
    return repo 

# Get Bad Recipe Repository
def get_bad_recipes(repo=Depends(BadRecipeRepository)):
    return repo