from fastapi import APIRouter
from sqlalchemy.sql.expression import false, select, update
from sqlalchemy.sql.functions import user
from ...schemas.schemas import Otp
from ...database.db import SessionLocal
from ...models.models import Otp as motp
from typing import Optional,List
from .send_email import  send_email
import math, random


router = APIRouter()

db = SessionLocal()

def generateOTP() :
     
    # Declare a digits variable 
    # which stores all digits
    digits = "123456789"
    OTP = ""
 
   # length can be changed by changing value in range
    for i in range(6) :
        OTP += digits[math.floor(random.random() * 10)]
        
    return OTP

@router.post("/request_otp/")
def request_otp(user:Otp):
    gotp = generateOTP()
    template = f"""

        Welcome To Waitbuddy !!!
        
        Thanks for using Waitbuddy here is your OTP: {gotp}
 
        """
    print(user.email)    
    entry = db.query(motp).filter(motp.email == user.email).first()
    if not entry:
        entry =  motp(email = user.email, otp = gotp)
        db.add(entry)
        db.commit()
    else:
        entry.otp = gotp 
        db.commit()
    return send_email('Here is your OTP' , str(user.email) , template)


@router.post("/verify_otp/")
def verify_otp(uotp:Otp):
    otp = db.query(motp).filter(motp.email == uotp.email).first()
    print(f"CheckThisOut!:: {otp}")
    if otp.otp == uotp.otp:
        return "Successfull"
    else:
        return f"Wrong Otp: {otp.otp} vs { uotp.otp }"
    
    


    
    