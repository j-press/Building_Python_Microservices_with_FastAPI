from enum import Enum

# Pydantic Category Model
class Category(str, Enum):
    """Category Model"""
    breakfast = "breakfast"
    lunch = "lunch"
    dinner = "dinner"
    appetizer = "appetizer"
    salad = "salad"
    entree = "entree"
    side_dish = "side_dish"
    pastry = "pastry"
    dessert = "dessert"
    snack = "snack"
    soup = "soup"
    holiday = "holiday"
    vegetarian = "vegetarian"
    cookbook = "cookbook"

# Pydantic Origin Model
class Origin(str, Enum):
    asian = "asian"
    mediterranean = "mediterranean"
    mid_eastern = "mid_eastern"
    african = "african"
    pacific = "pacific"
    south_american = "south_american"
    north_american = "north_american"
    european = "european"
    caribbean = "caribbean"
    indian = "indian"

# Pydantic UserType Model
class UserType(str, Enum):
    admin = "admin"
    user = "user"
    guest = "guest"

# Pydantic ReceipeRating Model
class RecipeRating(str, Enum):
    one = "1"
    two = "2"
    three = "3"
    four = "4"
    five = "5"
    