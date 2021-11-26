from fastapi import APIRouter


router = APIRouter()


@router.get("/home")
def create_job():
    return { 'Hello' : 'World!'}

