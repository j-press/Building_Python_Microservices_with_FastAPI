from datetime import datetime

from admin import manager
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse
from feedback import post
from handler_exceptions import PostFeedbackException, PostRatingException
from login import user
from places import destination
from starlette.exceptions import HTTPException as GlobalStarletteHTTPException
from tourist import visit

# FastAPI App
app = FastAPI()

# FastAPI Include Router for manager
app.include_router(manager.router)
# FastAPI Include Router for user
app.include_router(user.router)
# FastAPI Include Router for destination
app.include_router(destination.router)
# FastAPI Include Router for  visit
app.include_router(visit.router)
# FastAPI Include Router for post
app.include_router(post.router, prefix="/ch02/post")

# FastAPI middleware for handling HTTP 
@app.middleware("http")
async def log_transaction_filter(request: Request, call_next):
    start_time = datetime.now()
    method_name = request.method
    qp_map = request.query_params
    pp_map = request.path_params
    with open("request_log.txt", mode="a") as reqfile: 
        content = f"method: {method_name}, query param: {qp_map}, path params: {pp_map}, received at {datetime.now()}"
        reqfile.write(content)
    response = await call_next(request)
    process_time = datetime.now() - start_time 
    response.headers["X-Time-Elapsed"] = str(process_time)
    return response

# FastAPI GET Method for /ch02
@app.get("/ch02")
def index():
    return {"message": "Intelligent Tourist System Prototype!"}

# FastAPI Exception Handler for PostFeedbackException
@app.exception_handler(PostFeedbackException)
def feedback_exception_handler(req: Request, ex: PostFeedbackException):
    return JSONResponse(
        status_code=ex.status_code, 
        content={"message": f"error: {ex.detail}"}
    )

# FastAPI Exception Handler for GlobalStarletteHTTPException
def global_exception_handler(req: Request, ex: str):
    return PlainTextResponse(f"Error message: {ex}", status_code=400)

# FastAPI Exception Handler for RequestValidationError
@app.exception_handler(RequestValidationError)
def validationerror_exception_handler(req: Request, ex: str):
    return PlainTextResponse(f"Error message: {ex}", status_code=400)