from datetime import datetime
from os import name
from typing import Optional
from uuid import UUID
from fastapi.params import File
from pydantic import BaseModel
class UserModel(BaseModel): #serializer
    id:Optional[UUID]
    name:Optional[str]
    email:Optional[str]
    hashed_password:Optional[str]
    profile_picture: Optional[bytes]
    role: Optional[str]

    class Config:
        orm_mode=True 
        allow_population_by_field_name = True   
        
        
class StoreModel(BaseModel): #serializer
    id:Optional[UUID]
    owner_id: Optional[UUID]
    name:Optional[str]
    logo:Optional[str]
    address:Optional[str]
    category:Optional[str]
    openinghour: Optional[str]
    closinghour: Optional[str]

    class Config:
        orm_mode=True 
        allow_population_by_field_name = True          
        
        
class AppointmentModel(BaseModel): #serializer
    id:Optional[int]
    user_id:Optional[UUID]
    store_id: Optional[UUID]
    status:Optional[str]
    appointment_number:Optional[UUID]
    time_of_arrival:Optional[datetime]
    time_of_departure:Optional[datetime]
    date_created: Optional[datetime]

    class Config:
        orm_mode=True 
        allow_population_by_field_name = True                  
        
class Otp(BaseModel):
    id:Optional[int]
    user_id:Optional[UUID]
    email:Optional[str]
    expiry:Optional[datetime]
    name:Optional[str]
    phone:Optional[int]
    otp:Optional[int]  
    class Config:
        orm_mode = True      