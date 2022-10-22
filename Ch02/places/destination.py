from datetime import datetime
from enum import Enum, IntEnum
from typing import List, NamedTuple
from uuid import UUID, uuid4

from fastapi import APIRouter, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel

# FastAPI APIRouter
router = APIRouter()

# Empty Dict to store all the tours, basic info and locations 
tours = dict()
tours_basic_info = dict()
tours_locations = dict()

# Star Rating IntEnum
class StarRating(IntEnum):
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5

# Pydantic BaseModel for Post
class Post(BaseModel):
    feedback: str
    rating: StarRating
    date_posted: datetime

# Pydantic BaseModel for Location
class Location(BaseModel):
    latitude: float
    longitude: float = 0.0 

# Pydantic BaseModel for Tour Type
class TourType(str, Enum):
    resort = "resort"
    hotel = "hotel"
    bungalow = "bungalow"
    tent = "tent"
    exclusive = "exclusive"
    cruise = "cruise"
    villa = "villa"
    airbnb = "airbnb"
    hostel = "hostel"

# Pydantic BaseModel for Amenities Types 
class AmenitiesTypes(str, Enum):
    restaurant = "restaurant"
    pool = "pool"
    beach = "beach"
    shops = "shops"
    bars = "bars"
    activities = "activities"
    spa = "spa"
    gym = "gym"

# Pydantic BaseModel for Tour Input 
class TourInput(BaseModel):
    name: str
    city: str
    country: str
    type: TourType
    location: Location
    amenities: List[AmenitiesTypes]

# Pydantic BaseModel for Tour 
class Tour(BaseModel):
    id: UUID
    name: str 
    city: str
    country: str
    type: TourType 
    location: Location 
    amenities: List[AmenitiesTypes]
    feedbacks: List[Post]
    ratings: float 
    visits: int 
    isBooked: bool 

# Pydantic BaseModel for Tour Basic Info
class TourBasicInfo(BaseModel):
    id: UUID
    name: str 
    type: TourType 
    amenities: List[AmenitiesTypes]
    raitings: float 

# Pydantic BaseModel for Tour Location
class TourLocation(BaseModel):
    id: UUID
    name: str 
    city: str
    country: str 
    location: Location 

# Pydantic BaseModel for Tour Preference(str, Enum):
class TourPreference(str, Enum):
    party = "party"
    extreme = "hiking"
    staycation = "staycation"
    groups = "groups"
    solo = "solo"
    family = "family"
    romantic = "romantic"
    adventure = "adventure"
    luxury = "luxury"
    budget = "budget"


# FastAPI GET Method with APIRouter for list of destinations /ch02/destinations/list/all 
@router.get("/ch02/destinations/list/all")
def list_tour_destinations():
    tours_json = jsonable_encoder(tours)
    resp_headers = {'X-Access-Tours': 'Try Us', 'X-Contact-Details': '1-900-888-TOLL', 'Set-Cookie':'AppName=ITS; Max-Age=3600; Version=1'}
    return JSONResponse(content=tours_json, headers=resp_headers)

 # FastAPI Get Method with APIRouter for details of a destination /ch02/destinations/details/{id}
@router.get("/ch02/destinations/details/{id}")
def check_tour_profile(id: UUID):
    tour_info_json = jsonable_encoder(tours[id])
    return JSONResponse(content=tour_info_json)

# FastAPI Get Method with APIRouter for destination amenities /ch02/destinations/amenities/tour/{id}
@router.get("/ch02/destinations/amenities/tour/{id}")
def show_amenities(id: UUID):
    if tours[id].amenities != None:
        amenities = tours[id].amenities
        amenities_json = jsonable_encoder(tours[id].amenities)
        return JSONResponse(content=amenities_json)
    else:
        return {"message": "No amenities found for this tour"}

# FastAPI Get Method with APIRouter for mosted booked destination /ch02/destinations/mostbooked
@router.get("/ch02/destinations/mostbooked")
def check_recommended_tour(resp: Response):
    resp.headers['X-Access-Tours'] = 'TryUs'
    resp.headers['X-Contact-Details'] = '1-900-888-TOLL'
    resp.headers['Content-Language'] = 'en-US'
    ranked_desc_rates = sort_orders = sorted(tours.items(), key=lambda x: x[1].ratings, reverse=True)
    return ranked_desc_rates;
        