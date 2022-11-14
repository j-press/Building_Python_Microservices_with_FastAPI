from fastapi import Depends
from model.posts import Post
from repository.factory import get_post_repo 

# Post Service
class PostService:
    # Constructor
    def __init__(self, repo=Depends(get_post_repo)):
        self.repo = repo 

    # Add Post
    def add_post(self, post: Post):
        self.repot.insert_post(post)

    # Get Posts
    def get_post(self):
        return self.repo.query_posts()