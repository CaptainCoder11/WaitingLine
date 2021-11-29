from enum import Enum, IntEnum
from typing import Optional
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