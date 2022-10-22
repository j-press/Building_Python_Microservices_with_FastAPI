from uuid import UUID, uuid4

from background import audit_log_transaction
from fastapi import APIRouter, BackgroundTasks
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from handler_exceptions import PostFeedbackException, PostRatingException
from login.user import approved_users
from places.destination import Post, StarRating, tours
from pydantic import BaseModel
from utility import check_post_owner

# FastAPI APIRouter 
router = APIRouter()

# Pydantic BaseModel for Feedback for Tour
feedback_tour = dict()

class Assessment(BaseModel):
    id: UUID
    post: Post 
    tour_id: UUID
    tourist_id: UUID 

# FastAPI POST Method using APIRouter decorator for to add feedback  /feedback/add 
@router.post("/feedback/add")
def post_tourist_feedback(touristId: UUID, tid: UUID, post: Post, bg_task: BackgroundTasks):
    if approved_users.get(touristId) == None and tours.get(tid) == None:
        raise PostFeedbackException(detail='tourist and tour details not found', status_code=403)
    assessId = uuid4()
    assessment = Assessment(id=assessId, post=post, tour_id=tid, tourist_id=touristId)
    feedback_tour[assessId] = assessment
    tours[tid].ratings = (tours[tid].ratings + post.rating) / 2

    assess_json = jsonable_encoder(assessment)
    bg_task.add_task(audit_log_transaction, str(touristId), message="post_tourist_feedback")
    return JSONResponse(content=assess_json, status_code=200)

# FastAPI POST Method using APIRouter decorator for to update feedback rating /feedback/update/rating
@router.post("/feedback/update/rating")
def update_tour_rating(assessId: UUID, new_rating: StarRating):
    print(new_rating)
    if feedback_tour.get(assessId) == None: 
        raise PostRatingException(detail='tour assessment not found', status_code=403)
    tid = feedback_tour[assessId].tour_id
    tours[tid].ratings = (tours[tid].ratings + new_rating) / 2 
    tour_json = jsonable_encoder(tours[tid])
    return JSONResponse(content=tour_json, status_code=200)


# FastAPI DELETE Method using APIRouter decorator for to delete feedback /feedback/delete
@router.delete("/feedback/delete")
async def delete_tourist_feedback(assessId: UUID, touristId: UUID): 
    if approved_users.get(touristId) == None and feedback_tour.get(assessId): 
        raise PostFeedbackException(detail='tourist and tour details not found', status_code=403)
    post_delete = [assess for assess in feedback_tour.values() if assess.id == assessId]
    for access in post_delete: 
        is_owner = await check_post_owner(feedback_tour, access.id, touristId)
        if is_owner:
            del feedback_tour[access.id]
    return JSONResponse(content="Post deleted", status_code=200)

# FastAPI GET Method using APIRouter decorator for to get feedback /feedback/get
@router.get("/feedback/get")
async def get_tourist_feedback(touristId: UUID):
    print(feedback_tour)
    tourist_posts = [assess for assess in feedback_tour.values() if assess.tourist_id == touristId]
    tourist_posts_json = jsonable_encoder(tourist_posts)
    return JSONResponse(content=tourist_posts_json, status_code=200)
