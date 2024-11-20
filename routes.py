from models import Farmer
from models import Crop
from models import Crop_Log
from models import Device
from models import Notification
from models import Schedule
from fastapi import APIRouter, HTTPException, WebSocket, WebSocketDisconnect
from bson import ObjectId
from schema import *
from server import farmer
from server import crop
from server import device
from server import crop_log
from server import notification
from server import schedule
from datetime import datetime
from websocket import ConnectionManager
import json
router = APIRouter()
manager = ConnectionManager()

@router.get("/farmer")
async def get_farmer():
    farmers = farmer_list_serial(farmer.find())
    return farmers

@router.post("/farmer")
async def post_farmer(frm: Farmer):
    data = dict(frm)
    data['created_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
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

@router.post("/device")
async def post_dev(dev: Device):
    data = dict(dev)
    
    crop_data = crop_list_serial(crop.find())
    
    print(crop_data)
    
    for cropd in crop_data:
        print(cropd)
        if str(cropd['id']) in data['crop_id']:
            data['crop_id'] = str(cropd['id'])
            break
            
    result = device.insert_one(data)
    return {"code":200 if result else 204,
            "id": str(result.inserted_id)}

@router.get("/device")
async def get_device():
    try:
        # Fetch all devices from the database
        devices = device.find()
        
        # Serialize the list of devices
        serialized_devices = device_list_serial(devices)
        
        return serialized_devices
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/find_device")
async def get_device_by_id(id: str):
    try:
        # Find the device by its ID
        device_data = device.find_one({"_id": ObjectId(id)})

        if device_data:
            # Serialize the device data
            serialized_device = device_serial(device_data)
            return serialized_device
        else:
            raise HTTPException(status_code=404, detail="Device not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

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
async def get_notifications():
    # Fetch all notifications from the collection
    notifications = list(notification.find({}, {'_id': 0}))  # Exclude the _id field if you don't need it
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

@router.get("/crop/harvested")
async def get_harvested_crops():
    try:
        crops = list(crop.find({"crop_status": "harvested"}))
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
@router.get("/farmer/profile")
async def view_profile(farmer_id: str):
    try:
        result = farmer.find_one({"_id": ObjectId(farmer_id)})
        if not result:
            raise HTTPException(status_code=404, detail="Farmer not found")

        data = farmer_serial(result)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/farmer/{farmer_id}")
async def update_farmer(farmer_id: str, updated_data: Farmer):
    try:
        result = farmer.update_one(
            {"_id": ObjectId(farmer_id)},
            {"$set": updated_data.dict()}
        )
        
        if result.modified_count == 1:
            return {"message": "Farmer profile updated successfully."}
        else:
            raise HTTPException(status_code=404, detail="Farmer not found or no changes made.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/crop/planted")
async def get_planted_crops():
    try:
        crops = list(crop.find({"crop_status": "planted"}))
        if not crops:
            return []
        return crop_list_serial(crops)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/crop/{crop_name}/harvested")
async def update_crop_harvested(crop_name: str):
    try:
        result = crop.update_one({"crop_name": crop_name}, {"$set": {"crop_status": "harvested"}})
        return {"message": "Crop harvested"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/crop/{crop_name}/planted")
async def update_crop_status(crop_name: str):
    try:
        # Update the crop status to 'planted'
        result = crop.update_one({"crop_name": crop_name}, {"$set": {"crop_status": "planted"}})
        
        if result.modified_count == 1:
            # Fetch the updated crop data
            updated_crop = crop.find_one({"crop_name": crop_name})
            
            # Create the crop log entry
            log_entry = {
                "crop_name": updated_crop["crop_name"],
                "crop_date_planted": datetime.now().strftime('%Y-%m-%d %I:%M:%S %p'),  # Current timestamp as date planted
                "crop_date_harvested": None,  # Harvest date can be updated later when the crop is harvested
            }
            
            # Insert the log entry into the crop_log collection
            crop_log.insert_one(log_entry)
            
            return {"message": "Crop status updated to planted and log created."}
        else:
            raise HTTPException(status_code=404, detail="Crop not found")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.put("/crop_log/{crop_name}/harvested")
async def update_crop_log(crop_name: str):
    try:
        # Attempt to update the crop log where crop_date_harvested is null
        result = crop_log.update_one(
            {"crop_name": crop_name, "crop_date_harvested": None},
            {"$set": {"crop_date_harvested": datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')}}
        )
        
        # Check if an entry was modified
        if result.modified_count == 1:
            return {"message": "Crop log updated with harvest date."}
        else:
            return {"message": "No crop log entry found to update."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/crop_logs/delete_all")
async def delete_logs_except_unharvested():
    try:
        # Deleting logs where crop_date_harvested is not null
        result = crop_log.delete_many({"crop_date_harvested": {"$ne": None}})
        if result.deleted_count > 0:
            return {"message": f"Deleted {result.deleted_count} logs"}
        else:
            return {"message": "No logs to delete"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.delete("/notifications/delete_all")
async def delete_all_notifications():
    try:
        # Delete all notifications from the collection
        result = notification.delete_many({})
        if result.deleted_count > 0:
            return {"message": f"Deleted {result.deleted_count} notifications"}
        else:
            return {"message": "No notifications to delete"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.delete("/device/delete_all")
async def delete_device():
    try:
        result = device.delete_many({})
        if result.deleted_count:
            return {"message": f"Deleted {result.deleted_count} devices"}
        else:
            return {"message": "No devices to delete"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            received = await websocket.receive_text()
            
            timestamp = datetime.now().strftime("%I:%M %p")
            
            # json_data = json.loads(received)
            data = {
                "message": received,
                "timestamp": timestamp
            }
            
            # print(data["message"])
            try:
                sensor = json.loads(data["message"])
                # print(sensor["water_level"])
                
                if sensor["water_level"] == "Low":
                    notification.insert_one(data)
                    print(f"Message saved to DB: {received} at {timestamp}")
                elif sensor["soil_moisture"] >= 3000:
                    notification.insert_one(data)
                    print(f"Message saved to DB: {received} at {timestamp}")
            except json.JSONDecodeError:
                pass
                
            # if res:
            data = {
                "message": received,
                "timestamp": timestamp
            }
            # Broadcast the received data to all active connections
            print(data)
            await manager.broadcast(f"{json.dumps(data)}")
            print(f"Message received and broadcasted: {data}")
            
            

    except WebSocketDisconnect:
        manager.disconnect(websocket)  # Remove the client on disconnect
        print("WebSocket disconnected")
        
@router.websocket("/link")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            received = await websocket.receive_text()
            await manager.broadcast(received)

    except WebSocketDisconnect:
        manager.disconnect(websocket)  # Remove the client on disconnect
        print("WebSocket disconnected")
    
