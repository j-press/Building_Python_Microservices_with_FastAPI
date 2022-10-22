from fastapi import HTTPException


# FastAPI for Post Feedback HTTPException 
class PostFeedbackException(HTTPException):
    def __init__(self, detail: str, status_code: int):
        self.status_code = status_code 
        self.detail = detail 

# FastAPI for Post Rating HTTPException
class PostRatingException(HTTPException):
    def __init__(self, detail: str, status_code: int): 
        self.status_code = status_code
        self.detail = detail


