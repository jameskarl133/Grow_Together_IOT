from pydantic import BaseModel
from datetime import datetime

class Farmer(BaseModel):
    fname: str
    mname: str
    lname: str
    field_type: str
    dob: str
    email: str
    address: str
    phno: str
    username: str
    password: str
    status: str
    created_at: str = None
    updated_at: str = None

class Crop(BaseModel):
    crop_name:str
    # crop_image:str
    crop_soil:str
    # crop_soil_desc:str
    crop_moisture:str
    crop_temp:str
    crop_status:str
    # crop_created_at:str
    # crop_updated_at:str

class Crop_Log(BaseModel):
    crop_date_planted:str
    crop_date_harvested:str
    crop_name:str
    
class Notification(BaseModel):
    message:str
    date:str

class Schedule(BaseModel):
    sched_time:str