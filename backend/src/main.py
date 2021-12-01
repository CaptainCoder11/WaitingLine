from pydantic import main
from sqlalchemy.orm import Session
from .database.db import Base,engine,database
from fastapi import FastAPI,status,HTTPException
from .apis.version1.main_route import mainroute

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

app.include_router(mainroute)

