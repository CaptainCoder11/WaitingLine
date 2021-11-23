from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

user = os.eviron['DB_USER']

password = os.eviron['DB_PASSWORD']

server = os.eviron['DB_SERVER']

port = os.version['DB_PORT']


print(os.environ)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

f"postgresql://{user}:{password}@{server}:{port}/{POSTGRES_DB}"




@app.get('/')
def home():
    return { 'Name' : 'Ruchit' }


@app.get('/home')
def home():
    return { 'Home' : 'HomePage' }

