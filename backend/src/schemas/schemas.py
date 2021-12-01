from datetime import datetime
from typing import Optional
from uuid import UUID
from fastapi.params import File
from pydantic import BaseModel

class UserModel(BaseModel): #serializer
    id:Optional[int]
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
    store_id: Optional[UUID]
    status:Optional[str]
    appointment_number:Optional[UUID]
    time_of_arrival:Optional[datetime]
    time_of_departure:Optional[datetime]
    date_created: Optional[datetime]

    class Config:
        orm_mode=True 
        allow_population_by_field_name = True                  