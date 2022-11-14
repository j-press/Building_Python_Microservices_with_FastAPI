from uuid import UUID
from typing import List

# Keyword Dictionary
keywords_recipe = dict()

# Keyword Repository
class KeywordRepository: 
    def __init__(self):
        pass 
    # Insert Keyword
    def insert_keyword(self, id: UUID, keywords: List[str]):
        keywords_recipe[id] = keywords
    # Add Keywords
    def add_keywords(self, id: UUID, keyword: str):
        if keywords_recipe.get(id) == None:
            keywords = list()
            keywords.append(keyword)
            keywords_recipe[id] = keywords 
        else: 
            keywords = keywords_recipe[id]
            keywords.append(keyword)
            keywords_recipe[id] = keywords 
    
    # Get Keywords
    def query_keywords(self, id: UUID):
        return keywords_recipe[id]
    # Get All Keywords
    def query_all_keywords(self):
        return dict(keywords_recipe.items())