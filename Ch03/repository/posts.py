from datetime import date
from model.classifications import RecipeRating
from model.posts import Post 
from uuid import uuid4

# Dict to store all the posts
posts = dict()

# Post Repository
class PostRepository:
    def __init__(self):
        pass 

    # Insert Post
    def insert_post(self, post: Post):
        posts[post.id] = post

    # Get All Posts
    def query_posts(self):
        return list(posts.values())