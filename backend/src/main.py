from pydantic import main
from sqlalchemy.orm import Session
from .database.db import Base,engine,database
from fastapi import FastAPI,status,HTTPException
from .apis.version1.main_route import mainroute
from fastapi.middleware.cors import CORSMiddleware


def init_db():
    print("Creating database ....")
    Base.metadata.create_all(engine)
    
init_db()    

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(mainroute)

