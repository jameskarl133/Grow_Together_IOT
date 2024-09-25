from models import Farmer
from models import Crop
from models import Crop_Log
from models import Notification
from models import Schedule
from fastapi import APIRouter, HTTPException
from bson import ObjectId
from schema import *
from server import farmer
from server import crop
from server import crop_log
from server import notification
from server import schedule
from datetime import datetime
router = APIRouter()

@router.get("/farmer")
async def get_farmer():
    farmers = farmer_list_serial(farmer.find())
    return farmers

@router.post("/farmer")
async def post_farmer(frm: Farmer):
    data = dict(frm)
    # data = ['created_at'] = datetime.now()
    # data = ['updated_at'] = datetime.now()
    result = farmer.insert_one(data)
    return {"code": 200 if result else 204}

@router.get("/crop")
async def get_crop():
    crops = crop_list_serial(crop.find())
    return crops

@router.post("/crop")
async def post_crop(crp: Crop):
    data = dict(crp)
    result = crop.insert_one(data)
    return {"code": 200 if result else 204}

@router.get("/crop_log")
async def get_crop_log():
    crop_logs = crop_log_list_serial(crop_log.find())
    return crop_logs

@router.post("/crop_log")
async def post_crop_log(crp_lg: Crop_Log):
    data = dict(crp_lg)
    result = crop_log.insert_one(data)
    return {"code": 200 if result else 204}

@router.get("/notification")
async def get_notification():
    notifications = notification_list_serial(notification.find())
    return notifications

@router.post("/notification")
async def post_notification(notif: Notification):
    data = dict(notif)
    result = notification.insert_one(data)
    return {"code": 200 if result else 204}

@router.get("/schedule")
async def get_schedule():
    schedules = schedule_list_serial(schedule.find())
    return schedules

@router.post("/schedule")
async def post_schedule(sched: Schedule):
    data = dict(sched)
    result = schedule.insert_one(data)
    return {"code": 200 if result else 204}

@router.get("/crop/ondb")
async def get_ondb_crops():
    try:
        # Fetch crops that have the status "ondb"
        crops = list(crop.find({"crop_status": "ondb"}))
        serialized_crops = crop_list_serial(crops)
        return serialized_crops
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/farmer/login")
async def login_farmer(username: str, password: str):
    
    result = farmer.find_one({"username": username, "password": password})

    if result:
        
        data = {
            "id": str(result["_id"]),
            "username": result["username"],
            
        }
    else:
        
        raise HTTPException(status_code=401, detail="Invalid username or password")

    
    return {
        "access": True,
        "farmer": data
    }


@router.get("/crop/planted")
async def get_planted_crops():
    try:
        crops = list(crop.find({"crop_status": "planted"}))
        if not crops:
            return []
        return crop_list_serial(crops)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/crop/{crop_name}/planted")
async def update_crop_status(crop_name: str):
    try:
        result = crop.update_one({"crop_name": crop_name}, {"$set": {"crop_status": "planted"}})
        if result.modified_count == 1:
            return {"message": "Crop status updated to planted"}
        else:
            raise HTTPException(status_code=404, detail="Crop not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))