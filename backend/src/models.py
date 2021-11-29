from sqlalchemy.sql.sqltypes import LargeBinary
from .db import Base
from sqlalchemy import Boolean , Enum ,  Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from struct import *

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True , autoincrement=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    profile_picture = Column(LargeBinary)
    role = Column(Enum('OWNER','EMPLOYEE','REGULAR' , name = 'roles'))

    