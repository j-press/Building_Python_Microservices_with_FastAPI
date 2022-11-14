from uuid import UUID 
from model.classifications import Category, Origin 
from typing import List 

# Ingredient Model 
class Ingredient:
    def __init__(self, id: UUID, name: str, qty: float, measure: str):
        self.id = id
        self.name = name
        self.qty = qty
        self.measure = measure 

# Recipe Model
class Recipe: 
    def __init__(self, id: UUID, name: str, ingredient: List[Ingredient], category: Category, origin: Origin):
        self.id = id 
        self.name = name 
        self.ingredient = ingredient 
        self.category = category 
        self.origin = origin 