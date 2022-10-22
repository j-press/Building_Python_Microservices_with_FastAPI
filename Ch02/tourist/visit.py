from datetime import datetime
from typing import List
from uuid import UUID, uuid4

from fastapi import APIRouter, HTTPException, status
from login.user import approved_users
from places.destination import (TourBasicInfo, TourPreference, tours,
                                tours_locations)
from pydantic import BaseModel

# FastAPI APIRouter
router = APIRouter()

# Dict to store all tour preferences
tour_preferences = set()

# Pydantic BaseModel for Visit 
class Visit(BaseModel):
    id: UUID 
    destination: List[TourBasicInfo]
    last_tour: datetime 

# Pydantic BaseModel for Booking 
class Booking(BaseModel):
    id: UUID
    destination: TourBasicInfo
    booking_date: datetime
    tourist_id: UUID 

# FastAPI GET Method using APIRouter decorator for tourist tour preference ch02/tourist/tour/preference
@router.get("/ch02/tourist/tour/preference")
def make_tour_preferences(preference: TourPreference):
    tour_preferences.add(preference)
    return tour_preferences

# FastAPI POST Method using APIRouter decorator for adding tourist tour booking ch02/tourist/tour/booking/add
@router.post("/ch02/tourist/tour/booking/add")
def create_booking(tour: TourBasicInfo, touristId: UUID):
    if approved_users.get(touristId) == None: 
        raise HTTPException(status_code=500, detail="details are missing")
    booking = Booking(id=uuid4(), destination=tour, booking_date=datetime.now(), tourist_id=touristId)
    print(approved_users[touristId])
    approved_users[touristId]['tours'].append(tour)
    approved_users[touristId]['booked'] += 1
    tours[tour.id].isBooked = True
    tours[tour.id].visits += 1
    return booking

# FastAPI DELETE Method using APIRouter decorator for deleting tourist tour booking ch02/tourist/tour/booking/delete
@router.delete("/ch02/tourist/tour/booking/delete")
def remove_booking(bid: UUID, touristId: UUID):
    if approved_users.get(touristId) == None: 
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="details are missing")
    new_booking_list = [booked for booked in approved_users[touristId]['tours'] if booked.id == bid]
    approved_users[touristId]['tours'] = new_booking_list
    return approved_users[touristId]

# FastAPI GET Method using APIRouter decorator for tourist tour booking ch02/tourist/tour/booked
@router.get("/ch02/tourist/tour/booked")
def show_booked_tours(touristId: UUID):
    if approved_users.get(touristId) == None: 
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="details are missing", headers={"X-InputError":"missing tourist ID"})
    return approved_users[touristId]['tours']

# FastAPI GET Method using APIRouter decorator for tour location ch02/tourist/tour/location
@router.get("/ch02/tourist/tour/location")
def show_location(tid: UUID):
    return tours_locations[tid]

# FastAPI GET Method using APIRouter decorator for show available tours ch02/tourist/tour/available
@router.get("/ch02/tourist/tour/available")
def show_available_tours():
    available_tours = [t for t in tours.values() if t.isBooked == False]
    return available_tours
