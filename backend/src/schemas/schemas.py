from datetime import datetime
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
    id:Optional[int]
    owner_id: Optional[int]
    name:Optional[str]
    logo:Optional[bytes]
    address:Optional[str]
    category:Optional[str]
    openinghour: Optional[datetime]
    closinghour: Optional[datetime]

    class Config:
        orm_mode=True 
        allow_population_by_field_name = True          
        
        
class AppointmentModel(BaseModel): #serializer
    id:Optional[int]
    user_id:Optional[UUID]
    store_id: Optional[int]
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
    otp:Optional[int]  
    class Config:
        orm_mode = True      