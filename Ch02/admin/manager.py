from types import CoroutineType
from uuid import UUID, uuid4

from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from login.user import Signup, Tourist, User, approved_users, pending_users
from places.destination import (Tour, TourBasicInfo, TourInput, TourLocation,
                                tours, tours_basic_info, tours_locations)

router = APIRouter()

# FastAPI POST Method using APIRouter decorator for tour destination ch02/admin/destination/add
@router.post("/ch02/admin/destination/add")
def add_tour_destination(tour: TourInput):
    try:
        tid = uuid4()
        tour = Tour(id=tid, name=input.name, city=input.city, country=input.country, type=input.type, location=input.location, amenities=input.amenities, feedbacks=list(), ratings=0, visits=0, isBooked=False)
        tour_basic_info = TourBasicInfo(id=tid, name=input.name, type=input.type, amenities=input.amenities, ratings=0.0)
        tour_location = TourLocation(id=tid, name=input.name, city=input.city, country=input.country, location=input.location)
        tours[tid] = tour
        tours_basic_info[tid] = tour_basic_info
        tours_locations[tid] = tour_location
        tour_json = jsonable_encoder(tour)
        return JSONResponse(content=tour_json, status_code=status.HTTP_201_CREATED)
    except:
        return JSONResponse(content={"message": "Tour destination not created"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# FastAPI DELETE Method using APIRouter decorator for tour destination ch02/admin/destination/remove/{id}
@router.delete("/ch02/admin/destination/remove/{id}")
def remove_tour_destination(id: UUID):
    try: 
        del tours[id]
        del tours_basic_info[id]
        del tours_locations[id]
        return JSONResponse(content={"message": "Tour destination removed"}, status_code=status.HTTP_202_ACCEPTED)
    except:
        return JSONResponse(content={"message": "Tour destination not removed"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

# FastAPI PUT Method using APIRouter decorator for tour destination ch02/admin/destination/update
@router.put("/ch02/admin/destination/update", status_code=status.HTTP_202_ACCEPTED)
def update_tour_destination(tour: Tour):
    try: 
        tid = tour.id
        tours[tid] = tour
        tour_basic_info = TourBasicInfo(id=tid, name=tour.name, type=tour.type, amenities=tour.amenities, ratings=tour.ratings)
        tour_location = TourLocation(id=tid, name=tour.name, city=tour.city, country=tour.country, location=tour.location)
        tours_basic_info[tid] = tour_basic_info
        tours_locations[tid] = tour_location
        return {"message": "Tour destination updated"}
    except:
        return {"message": "Tour destination not updated"}


#FastAPI GET Method using APIRouter decorator for listing all destinations ch02/admin/destination/list
@router.get("/ch02/admin/destination/list", status_code=status.HTTP_200_OK)
def list_all_tours():
    return tours # returns all tours, but with no semi-colon?

# FastAPI GET Method using APIRouter decorator for listing all tourist ch02/admin/tourist/list
@router.get("/ch02/admin/tourist/list", status_code=status.HTTP_200_OK)
def list_all_tourists():
    return approved_users; # returns all approved users with semi-colon? 

# FastAPI GET Method using APIRouter decorator for listing all pending tourist ch02/admin/tourist/pending/list
@router.get("/ch02/admin/tourist/pending/list", status_code=status.HTTP_200_OK)
def list_all_pending_tourists():
    return pending_users;



# FastAPI GET Method using APIRouter decorator for tourist vip status ch02/admin/tourist/vip
@router.get("/ch02/admin/tourist/vip")
def list_valuable_tourists():
    try: 
        sort_orders = sorted(approved_users.items(), key=lambda x: x[1].booked, reverse=True)
        sorted_orders_json = jsonable_encoder(sort_orders)
        return JSONResponse(content=sorted_orders_json, status_code=status.HTTP_200_OK)
    except:
        return JSONResponse(content={"message": "No VIP Tourists were found"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# FastAPI POST Method using APIRouter decorator for approved user ch02/admin/user/login/approve
@router.post("/ch02/admin/user/login/approve")
def approve_login(userid: UUID):
    try: 
        approved_users[userid] = pending_users[userid]
        del pending_users[userid]
        return JSONResponse(content={"message": "User approved"}, status_code=status.HTTP_200_OK)
    except:
        return JSONResponse(content={"message": "User not approved"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

""" # FastAPI Get Method using APIRouter decorator for /ch02/admin/tourist/list
@router.get("/tourist/list")
def list_all_tourists():
    return approved_users
 """

""" # FastAPI PUT Method using APIRouter decorator for /ch02/admin/destination/update
@router.put("/ch02/admin/destination/update", status_code=status.HTTP_202_ACCEPTED)
def update_tour_destination(tour: Tour):
    try: 
        tid = tour.id 
        tours[tid] = tour
        tour_basic_info = TourBasicInfo(id=tid, name=tour.name, type=tour.type, amenities=tour.amenities, ratings=tour.ratings)
        tour_location = TourLocation(id=tid, name=tour.name, city=tour.city, country=tour.country, location=tour.location)
        tours_basic_info[tid] = tour_basic_info
        tours_locations[tid] = tour_location
        return {"message": "Tour updated successfully"}
    except:
        return {"message": "Tour not found"} """