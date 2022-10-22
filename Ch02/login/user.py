from datetime import datetime
from typing import List
from uuid import UUID, uuid4

from background import audit_log_transaction
from fastapi import APIRouter, BackgroundTasks, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from places.destination import TourBasicInfo
from pydantic import BaseModel

# FastAPI APIRouter 
router = APIRouter()

# Dict to store all the approved users and pending users
pending_users = dict()
approved_users = dict()

# Pydantic BaseModel for Singup
class Signup(BaseModel):
    username: str
    password: str
    firstname: str
    lastname: str
    birthday: datetime

# Pydantic BaseModel for User 
class User(BaseModel):
    id: UUID
    username: str
    password: str
    
# Pydantic BaseModel for Tourst
class Tourist(BaseModel):
    id: UUID 
    login: User
    date_signed: datetime
    booked: int 
    tours: List[TourBasicInfo]

# FastAPI POST Method using APIRouter decorator for user signup ch02/user/signup
@router.post("/ch02/user/signup")
def signup(signup: Signup):
    try: 
        userid = uuid4()
        login = User(id=userid, username=signup.username, password=signup.password)
        tourist = Tourist(id=userid, login=login, date_signed=datetime.now(), booked=0, tours=list())
        tourist_json = jsonable_encoder(tourist)
        pending_users[userid] = tourist_json 
        return JSONResponse(content=tourist_json, status_code=status.HTTP_201_CREATED)
    except:
        return JSONResponse(content={"message": "User not created"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

# FastAPI POST Method using APIRouter decorator for user login ch02/user/login
@router.post("/ch02/user/login")
def login(login: User, bg_task: BackgroundTasks):
    try: 
        signup_json = jsonable_encoder(approved_users[login.id])
        bg_task.add_task(audit_log_transaction, touristId=str(login.id), message="User logged in")
        return JSONResponse(content=signup_json, status_code=status.HTTP_200_OK)
    except:
        return JSONResponse(content={"message": "Invalid operation"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

# FastAPI Get Method using APIRouter decorator for user list ch02/user/login/{username}/{password}
@router.get("/ch02/user/login/{username}/{password}")
def login(username: str, password: str, bg_task: BackgroundTasks):
    tourist_list = [ tourist for tourist in approved_users.values() if tourist['login']['username'] == username and tourist['login']['password'] == password]
    if len(tourist_list) == 0 or tourist_list == None: 
        return JSONResponse(content={"message": "Invalid operation"}, status_code=status.HTTP_403_FORBIDDEN)
    else:
        tourist = tourist_list[0]
        tour_json = jsonable_encoder(tourist)
        bg_task.add_task(audit_log_transaction, touristId=str(tourist['login']['id']), message="User logged in")
        return JSONResponse(content=tour_json, status_code=status.HTTP_200_OK)
