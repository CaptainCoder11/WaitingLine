

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return { 'Name' : 'Ruchit' }


@app.get('/home')
def home():
    return { 'Home' : 'HomePage' }

