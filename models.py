from pydantic import BaseModel

class Farmer(BaseModel):
    fname:str
    mname:str
    lname:str
    dob:str
    email:str
    address:str
    phno:str
    username:str
    password:str
    status:str
    created_at:str
    updated_at:str
    img:str

class Crop(BaseModel):
    crop_name:str
    crop_image:str
    crop_soil:str
    crop_moisture:str
    crop_temp:str
    crop_status:str
    crop_created_at:str
    crop_updated_at:str
    