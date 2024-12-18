import datetime

#farmer db schema
def farmer_serial(farmer) -> dict:
    return {
        "id": str(farmer["_id"]),
        "fname": str(farmer["fname"]),
        "mname": str(farmer.get("mname", "")),
        "lname": str(farmer["lname"]),
        "field_type": str(farmer["field_type"]),
        "dob": str(farmer["dob"]),
        # "email": str(farmer["email"]),
        "address": str(farmer["address"]),
        "phno": str(farmer["phno"]),
        "username": str(farmer["username"]),
        "password": str(farmer["password"]),
        "status": str(farmer["status"]),
        "security_question": str(farmer["security_question"]),  # Add this field
        "security_answer": str(farmer["security_answer"]),  # Add this field
        "created_at": str(farmer.get("created_at", "")),
        "updated_at": str(farmer.get("updated_at", ""))
    }

def farmer_list_serial(farmers) -> list:
    return [farmer_serial(farmer) for farmer in farmers]

#crop db schema
def crop_serial(crop) -> dict:
    return{
        "id":str(crop["_id"]),
        "crop_name":str(crop["crop_name"]),
        # "crop_image":str(crop["image"]),
        "crop_soil":str(crop["crop_soil"]),
        # "crop_soil_desc": str(crop["crop_soil_desc"]),
        "crop_moisture":str(crop["crop_moisture"]),
        "crop_temp":str(crop["crop_temp"]),
        "crop_status":str(crop["crop_status"]),
        "crop_estdate":str(crop["crop_estdate"]),
        # "crop_days_grown":str(crop["crop_days_grown"])
        # "crop_created_at":str(crop["crop_created_at"]),
        # "crop_updated_at":str(crop["crop_updated_at"]),
        
    }

def crop_list_serial(crops) -> list:
    return [crop_serial(crop) for crop in crops]

#crop_log db schema
def crop_log_serial(crop_log) -> dict:
    return{
        "crop_date_planted":str(crop_log["crop_date_planted"]),
        "crop_date_harvested":str(crop_log["crop_date_harvested"]),
        "crop_name":str(crop_log["crop_name"])
    }

def crop_log_list_serial(crop_logs) -> list:
    return [crop_log_serial(crop_log) for crop_log in crop_logs]

#notification db schema
def notification_list_serial(notification) -> dict:
    return{
        "message":str(notification["message"]),
        "date":str(notification["date"])
    }

def notification_list_serial(notifications) -> list:
    return [notification_list_serial(notification) for notification in notifications]

#schedule db shcema
def schedule_list_serial(schedule) -> dict:
    return{
        "sched_time":str(schedule["sched_time"])
    }

def schedule_list_serial(schedules) -> list:
    return[schedule_list_serial(schedule) for schedule in schedules]

def device_serial(device) -> dict:
    return {
        "id": str(device["_id"]),
        "device_name": str(device["device_name"]),
        "crop_id": str(device["crop_id"]),
        "mac_ad": str(device["mac_ad"])
    }

def device_list_serial(devices) -> list:
    return [device_serial(device) for device in devices]