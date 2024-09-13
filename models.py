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