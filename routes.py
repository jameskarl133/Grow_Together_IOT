from models import Farmer
from fastapi import APIRouter
from bson import ObjectId
from schema import *
from server import farmer
router = APIRouter()

@router.get("/farmer")
async def get_farmer():
    farmers = farmer_list_serial(farmer.find())
    return farmers

@router.post("/farmer")
async def post_farmer(frm: Farmer):
    print('test')
    data = dict(frm)
    result = farmer.insert_one(data)
    return{
        "code" : 200 if result else 204
    }