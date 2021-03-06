from datetime import datetime
from fastapi import APIRouter
from sqlalchemy.sql.expression import false, select
from ...schemas.schemas import StoreModel
from ...models.models import Store as self_store
from ...database.db import SessionLocal
from typing import Optional,List
from sqlalchemy.orm.exc import UnmappedClassError, UnmappedInstanceError


router = APIRouter()

db = SessionLocal()

@router.post("/add_store/" , response_model= StoreModel)
def add_store(store : StoreModel):
    print(store)
    openinghour = '10:00:00'
    closinghour = '22:00:00'
    s = self_store(name = store.name , logo = store.logo , address = store.address , 
              category = store.category , 
              openinghour = openinghour,
              closinghour = closinghour)
    db.add(s)
    db.commit()
    return s

@router.get('/get_store/')
def get_store():
    return db.query(self_store).offset(0).limit(100).all()

@router.get("/get_appointments/{store_id}")
def get_user(store_id : int):
    return db.query(self_store).filter(self_store.id == store_id).all()
    

