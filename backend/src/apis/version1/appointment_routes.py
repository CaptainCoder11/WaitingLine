from datetime import datetime
from fastapi import APIRouter
from sqlalchemy.sql.expression import false, select
from ...schemas.schemas import AppointmentModel
from ...database.db import SessionLocal
from ...models.models import Appointment as appointment
from typing import Optional,List
from sqlalchemy.orm.exc import UnmappedClassError, UnmappedInstanceError


router = APIRouter()

db = SessionLocal()

@router.post("/add_appointment/" , response_model= AppointmentModel)
def create_user(appt : AppointmentModel):
    print(appt)
    arrival = datetime.now()
    mappt = appointment(user_id = appt.user_id,
                       store_id = appt.store_id , 
                       status = appt.status ,
                       time_of_arrival = arrival , 
                       time_of_departure = appt.time_of_departure , 
                       date_created = appt.time_of_arrival)
    db.add(mappt)
    db.commit()
    return mappt
    

@router.post("/get_appointments")
def get_user(appt : AppointmentModel):
    return db.query(appointment).filter(appointment.store_id == appt.store_id).all()

@router.get("/get_appointments/")
def get_user():
    return db.query(appointment).offset(0).limit(100).all()

@router.get("/clear_appointments/")
def clear_appointments():
    db.__appointment__.drop()
    
