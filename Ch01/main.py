
from enum import Enum
from typing import Dict, List, Optional
from uuid import UUID, uuid4

from bcrypt import checkpw, gensalt, hashpw
from datetime import date, datetime


from fastapi import Cookie, FastAPI, Header, Response
from pydantic import BaseModel

from string import ascii_lowercase
from random import random


app = FastAPI()

valid_users = dict()
valid_profiles = dict()
pending_users = dict()
discussion_post = dict()
request_headers = dict()
cookies = dict()



# Pydantic models User, Validuser, UserType, UserProfile, PostType, ForumPost, ForumDiscussion
class User(BaseModel):
    username: str
    password: str

class ValidUser(BaseModel):
    id: UUID
    username: str
    password: str
    passphrase: str

class UserType(str, Enum):
    admin = "admin"
    teacher = "teacher"
    alumni = "alumni"
    student = "student"

# Pydantic UserProfile model
class UserProfile(BaseModel):
    firstname: str
    lastname: str
    middle_initial: str
    age: Optional[int] = 0
    salary: Optional[int] = 0
    birthday: date 
    user_type: UserType 

# Pydantic PostType model
class PostType(str, Enum):
    information = "information"
    inquiry = "inquiry"
    quote = "quote"
    twit = "twit"


# Pydantic Post model
class Post(BaseModel):
    topic: Optional[str] = None
    message: str 
    date_posted: datetime

# Pydantic ForumPost model
class ForumPost(BaseModel):
    id: UUID
    topic: Optional[str] = None
    message: str
    post_type: PostType
    date_posted: datetime 
    username: str 

# Pydantic ForumDiscussion model
class ForumDiscussion(BaseModel):
    id: UUID 
    main_post: ForumPost
    replies: Optional[List[ForumPost]] = None
    author: UserProfile





@app.get("/ch01/index")
def index():
    return {"message": "Welcome FastAPI Nerds"}


# FastAPI POST Method to create a new user /ch01/login/singup
@app.post("/ch01/login/signup")
def singup(uname: str, passwd: str):
    if (uname == None and passwd == None):
        return {"message": "Please enter a username and password"}
    elif (uname == None):
        return {"message": "Please enter a username"}
    elif (passwd == None):
        return {"message": "Please enter a password"}
    else:
        user = User(username=uname, password=passwd)
        pending_users[uname] = user 
        return user 

# FastAPI POST Method for Pending User to create a new user /ch01/list/users/pending
@app.post("/ch01/list/users/pending")
def list_pending_user():
    return pending_users

# FastAPI DELETE Method for Pending User to delete a new user /ch01/delete/users/pending
@app.delete("/ch01/delete/users/pending")
def delete_pending_users(accounts: List[str] = []):
    for user in accounts:
        del pending_users[user]
    return {"message": "deleted pending users"}


# FastAPI POST Method for Valid User /ch01/login/validate 
@app.post("/ch01/login/validate")
def approve_user(user: User): 
    if not valid_users.get(user.username) == None:
        return ValidUser(id=None, username=None, password=None, passphrase=None)
    else: 
        valid_user = ValidUser(id=uuid4(), username=user.username, password=user.password, passphrase= hashpw(user.password.encode(), gensalt()))
        valid_users[user.username] = valid_user
        del pending_users[user.username]
        return valid_user

# FastAPI DELETE Method for all users /ch01/login/remove/all
@app.delete("/ch01/login/remove/all")
def delete_user(usernames: List[str]):
    for user in usernames:
        del valid_users[user]
    return {"message": "deleted users"}

# FastAPI DELETE Method for a single user /ch01/login/remove/{username}
@app.delete("/ch01/login/remove/{username}")
def delete_user(username: str):
    if username == None:
        return {"message": "Please enter a username"}
    else:
        del valid_users[username]
        return {"message": "deleted user"}

# FastAPI GET Method for all users /ch01/list/users/valid
@app.get("/ch01/list/users/valid")
def list_valid_user():
    return valid_users


# FastAPI Get METHOD for login /ch01/login
@app.get("/ch01/login")
def login(username: str, password: str):
    if valid_users.get(username) == None: 
        return {"message": "user does not exist"}
    else:
        user = valid_users.get(username)
        if checkpw(password.encode(), user.password.encode()):
            return user
            #return {"message": "Welcome, {}".format(user.username)}
        else:
            return {"message": "invalid user"}

# FastAPI POST METHOD for login /ch01/login
@app.post("/ch01/login")
def signup(uname: str, passwd: str):
    if (uname == None and passwd == None):
        return {"message": "Please enter username and password"}
    elif (uname == None):
        return {"message": "Please enter username"}
    elif (passwd == None):
        return {"message": "Please enter password"}
    else:
        user = User(username=uname, password=passwd)
        pending_users[uname] = user
        return user

# FastAPI PUT METHOD for updating user account /ch01/account
@app.put("/ch01/account/profile/update/{username}")
def update_profile(username: str, id: UUID, new_profile: UserProfile):
    if valid_users.get(username) == None:
        return {"message": "user does not exist"}
    else:
        user = valid_users.get(username)
        if user.id == id:
            valid_profiles[username] = new_profile
            return {"message": "Profile succssfully updated"}
        else:
            return {"message": "user does not exist"}

# FastAPI PATCH METHOD for updating user account /ch01/account
@app.patch("/ch01/account/profile/update/names/{username}")
def update_profile_names(username: str, id: UUID, new_names: Dict[str, str]):
    if valid_users.get(username) == None:
        return {"message": "user does not exist"}
    elif new_names == None:
        return {"message": "Please enter new names"}
    else:
        user = valid_users.get(username)
        if user.id == id:
            profile = valid_users[username]
            profile.firstname = new_names['fname']
            profile.lastname = new_names['lname']
            profile.middle_initial = new_names['minit']
            valid_profiles[username] = profile
            return {"message": "Profile succssfully updated"}
        else:
            return {"message": "user does not exist"}

# should be above /ch01/login/{username}/{password}
@app.get("/ch01/login/details/info")
def login_info():
    return {"message": "username and password are needed"}

# should be above /ch01/login/{username}/{password}
@app.get("/ch01/login/password/change")
def change_password(username: str, old_passw: str = '', new_passw: str = ''):
    passwd_len = 8
    if valid_users.get(username) == None:
        return {"message": "user does not exist"}
    elif old_passw == '' or new_passw == '':
        characters = ascii_lowercase
        temporary_passwd = ''.join(random.choice(characters) for i in range(passwd_len))
        user = valid_users.get(username)
        user.password = temporary_passwd
        user.passphrase = hashpw(temporary_passwd.encode(),gensalt())
        return user
    else:
        user = valid_users.get(username)
        if user.password == old_passw:
            user.password = new_passw
            user.passphrase = hashpw(new_passw.encode(),gensalt())
            return user
        else:
            return {"message": "invalid user"}

# should be above /ch01/login/{username}/{password}
@app.post("/ch01/login/username/unlock")
def unlock_username(id: Optional[UUID] = None):
    if id == None:
        return {"message": "token needed"}
    else:
        for key, val in valid_users.items():
            if val.id == id:
                return {"username": val.username}
        return {"message": "user does not exist"}

# should be above /ch01/login/{username}/{password}
@app.post("/ch01/login/password/unlock")
def unlock_password(username: Optional[str] = None, id: Optional[UUID] = None ):
    if username == None:
        return {"message": "username is required"}
    elif valid_users.get(username) == None:
        return {"message": "user does not exist"}
    else:
        if id == None:
            return {"message": "token needed"}
        else:
            user = valid_users.get(username)
            if user.id == id:
                return {"password": user.password}
            else:
                return {"message": "invalid token"}
            
@app.get("/ch01/login/{username}/{password}")
def login_with_token(username: str, password:str, id: UUID):
    if valid_users.get(username) == None:
        return {"message": "user does not exist"}
    else:
        user = valid_users[username]
        if user.id == id and checkpw(password.encode(), user.passphrase):
            return user
        else:
            return {"message": "invalid user"}





# FastAPI HEADERS for Verify User /ch01/verify
@app.get("/ch01/headers/verify")
def verify_headers(host: Optional[str] = Header(None), 
                   accept: Optional[str] = Header(None), 
                   accept_language: Optional[str] = Header(None), 
                   accept_encoding: Optional[str] = Header(None), 
                   user_agent: Optional[str] = Header(None)):
    request_headers["Host"] = host
    request_headers["Accept"] = accept
    request_headers["Accept-Language"] = accept_language
    request_headers["Accept-Encoding"] = accept_encoding
    request_headers["User-Agent"] = user_agent
    return request_headers
   
   

# FastAPI POST METHOD for creating a new user account /ch01/account/profile/add
@app.post("/ch01/account/profile/add", response_model=UserProfile)
def add_profile(uname: str, 
                fname: str = Form(...), 
                lname: str = Form(...), 
                mid_init: str = Form(...), 
                user_age: int = Form(...),
                sal: float = Form(...), 
                bday: str = Form(...), 
                utype: UserType = Form(...)):
    if valid_users.get(uname) == None: 
        return UserProfile(firstname=None, lastname=None, middle_initial=None, age=None, birthday=None, salary=None, user_type=None)
    else:
        profile = UserProfile(firstname=fname, lastname=lname, middle_initial=mid_init, age=user_age, birthday=datetime.strptime(bday, '%m/%d/%Y'), salary=sal, user_type=utype)
        valid_profiles[uname] = profile 
        return profile

    
# FastAPI Cookie for Post /ch01/login/rememberme/create/ 
@app.post("/ch01/login/rememberme/create/")
def create_cookes(resp: Response, id: UUID, username: str = ''):
    resp.set_cookie(key="userkey", value=username)
    resp.set_cookie(key="identity", value=str(id))
    return {"message": "remember-me tokens created"}

# FastAPI Cookie for Get Method /ch01/login/cookies
@app.get("/ch01/login/cookies")
def access_cookie(userkey: Optional[str] = Cookie(None), identity: Optional[str] = Cookie(None)):
    cookies["userkey"] = userkey
    cookies["identity"] = identity 
    return cookies 