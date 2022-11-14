from fastapi import FastAPI, Depends
from api import recipes, users, posts, keywords, complaints, admin, admin_mcontainer, login
from dependencies.global_transactions import log_tranaction

# Create FastAPI Application
app = FastAPI(dependencies=[Depends(log_tranaction)])

# Register API Routes
app.include_router(recipes.router, prefix="/Ch03")
app.include_router(users.router, prefix="/Ch03")
app.include_router(posts.router, prefix="/Ch03")
app.include_router(keywords.router, prefix="/Ch03")
app.include_router(complaints.router, prefix="/Ch03")
app.include_router(admin.router, prefix="/Ch03")
app.include_router(admin_mcontainer.router, prefix="/Ch03")
app.include_router(login.router, prefix="/Ch03")

# Run Application
@app.get("/Ch03")
def index():
    return {"message": "Welcome to the Recipe API"}