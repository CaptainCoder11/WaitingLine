from sqlalchemy.orm import Session
from .db import Base,engine
from fastapi import FastAPI,status,HTTPException
from .db import SessionLocal,database
from .apis.base import api_router

def init_db():
    print("Creating database ....")
    Base.metadata.create_all(engine)
    
init_db()    

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(api_router)

