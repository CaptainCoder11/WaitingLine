from sqlalchemy.sql.expression import false, true
from sqlalchemy.sql.sqltypes import BigInteger, Date, DateTime, LargeBinary
from ..database.db import Base
from sqlalchemy import Boolean , Enum ,  Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from struct import *
import uuid

"""
class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), default=uuid.uuid4)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    profile_picture = Column(LargeBinary)
    role = Column(Enum('OWNER','EMPLOYEE','REGULAR' , name = 'roles'))
"""
    
class Store(Base):
    __tablename__ = "store"
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=true)
    owner_id = Column(UUID(as_uuid=True), default=uuid.uuid4)
    name = Column(String , nullable= false)
    logo = Column(String)
    address = Column(String, index=True , nullable=false)
    category = Column(String , nullable=false)
    openinghour = Column(String)
    closinghour = Column(String)
    
     
class Appointment(Base):
    __tablename__ = "appointment"
    id = Column(Integer, primary_key= True, index= True , autoincrement= True)
    user_id = Column(UUID(as_uuid=True), default=uuid.uuid4)
    store_id = Column(UUID(as_uuid=True), default=uuid.uuid4)
    status = Column(Enum('In_Queue','In_Store','Cancelled','Rejected','Departed' , name = 'status'))  
    appointment_number = Column(UUID(as_uuid=True), default=uuid.uuid4)
    time_of_arrival = Column(DateTime)
    time_of_departure = Column(DateTime)
    date_created = Column(DateTime)
    
class Otp(Base):
    __tablename__ = "Otp"
    id = Column(Integer, primary_key=True, index=True , autoincrement=True)
    user_id = Column(UUID(as_uuid=True), default=uuid.uuid4)
    name = Column(String)
    expiry_time = Column(DateTime)
    email = Column(String, unique=True, index=True)
    phone = Column(BigInteger,unique=True,index=True)
    otp = Column(Integer , nullable=false)  

    