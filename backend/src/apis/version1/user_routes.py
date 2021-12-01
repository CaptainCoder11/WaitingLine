from fastapi import APIRouter
from sqlalchemy.sql.expression import false, select
from ...schemas.schemas import UserModel
from ...database.db import SessionLocal
from ...models.models import User as u
from typing import Optional,List
from sqlalchemy.orm.exc import UnmappedClassError, UnmappedInstanceError


router = APIRouter()

db = SessionLocal()

@router.post("/add_user/" , response_model= UserModel)
def create_user(user : UserModel):
    print(user)
    picture = user.profile_picture
    user = u(name = user.name , email = user.email , hashed_password = user.hashed_password, profile_picture = picture , role = user.role )
    db.add(user)
    db.commit()
    return user
    

@router.get("/get_user/")
def get_user():
    return db.query(u).offset(0).limit(100).all()

@router.post("/get_user_id")
def get_user_id(user : UserModel):
    return db.query(u).filter(u.id == user.id).first()


@router.post("/check_login")
def check_login(user: UserModel):
    res = db.query(u).filter(u.email == user.email).first()
    if res.hashed_password == user.hashed_password:
        return "Login Successful!"
    else:
        return "Login Failed!"

