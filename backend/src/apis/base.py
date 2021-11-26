from  .version1.route_jobs import router
from fastapi import APIRouter


api_router = APIRouter()

api_router.include_router(router)