from datetime import datetime , date , timedelta
from os import name
from fastapi import APIRouter
from sqlalchemy.sql.expression import false, select, update
from sqlalchemy.sql.functions import user
from sqlalchemy.sql.operators import op
from ...schemas.schemas import Otp
from ...database.db import SessionLocal
from ...models.models import Otp as motp
from typing import Optional,List
from .send_email import  send_email
import math, random
import pyotp

router = APIRouter()

db = SessionLocal()

totp = pyotp.TOTP('base32secret3232')

@router.post("/request_otp/")
def request_otp(user:Otp):
    expiry_time = datetime.now() + timedelta(minutes = 10)
    gotp = totp.at(expiry_time)
    
    template = f"""
    
        Welcome To Waitbuddy !!!
        
        Thanks for using Waitbuddy here is your OTP: {gotp}
 
        """
        
    print(user.email)    
    
    entry = db.query(motp).filter(motp.email == user.email).first()
    if not entry:
        print(f"does not exist:{gotp}")
        entry =  motp(email = user.email, name= user.name , expiry_time = expiry_time, phone = user.phone ,  otp = gotp)
        db.add(entry)
        db.commit()
    else:
        print("User exist")
        entry.otp = gotp 
        db.commit()
    return send_email('Here is your OTP' , str(user.email) , template)


@router.post("/verify_otp/")
def verify_otp(uotp:Otp):
    time = datetime.now()
    otp = db.query(motp).filter(motp.email == uotp.email).first()
    print(f"CheckThisOut!:: {otp}")
    if otp.otp == uotp.otp and otp.expiry_time < time:
        return otp
    elif otp.otp == uotp.otp and otp.expiry_time > time:
        return "OTP Expired!"
    else:
        return f"Wrong Otp: {otp.otp} vs { uotp.otp }"
    
    
    


    
    