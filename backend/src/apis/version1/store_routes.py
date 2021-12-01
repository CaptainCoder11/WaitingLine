from fastapi import APIRouter
from sqlalchemy.sql.expression import false, select
from ...schemas.schemas import StoreModel
from ...models.models import Store as self_store
from ...database.db import SessionLocal
from ...models.models import Store as store
from typing import Optional,List
from sqlalchemy.orm.exc import UnmappedClassError, UnmappedInstanceError


router = APIRouter()

db = SessionLocal()

@router.post("/add_store/" , response_model= StoreModel)
def add_store(store : StoreModel):
    print(store)
    s = self_store(name = store.name , logo = store.logo , 
              address = store.address , category = store.category ,
              openinghour = store.openinghour , closinghour = store.closinghour )
    db.add(s)
    db.commit()
    return s

@router.get('/get_store/')
def get_store():
    return db.query(self_store).offset(0).limit(100).all()




