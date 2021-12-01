from fastapi import APIRouter
from ..version1.user_routes import router as Userroutes
from ..version1.store_routes import router as Storeroutes
from ..version1.appointment_routes import router as Appointmentroutes

mainroute = APIRouter()

mainroute.include_router(Userroutes)
mainroute.include_router(Storeroutes)
mainroute.include_router(Appointmentroutes)