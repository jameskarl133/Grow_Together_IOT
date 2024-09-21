#farmer db schema
def farmer_serial(farmer) -> dict:
    return{
        "id":str(farmer["_id"]),
        "fname":str(farmer["fname"]),
        "mname":str(farmer["mname"]),
        "lname":str(farmer["lname"]),
        # "field_type":str(farmer["field_type"]),
        "dob":str(farmer["dob"]),
        "email":str(farmer["email"]),
        "address":str(farmer["address"]),
        "phno":str(farmer["phno"]),
        "username":str(farmer["username"]),
        "password":str(farmer["password"]),
        "status":str(farmer["status"]),
        # "created_at":str(farmer["created_at"]),
        # "updated_at":str(farmer["updated_at"]),
        
    }

def farmer_list_serial(farmers) -> list:
    return [farmer_serial(farmer) for farmer in farmers]

#crop db schema
def crop_serial(crop) -> dict:
    return{
        "id":str(crop["_id"]),
        "crop_name":str(crop["name"]),
        "crop_image":str(crop["image"]),
        "crop_soil":str(crop["crop_soil"]),
        "crop_soil_description": str(crop["crop_soil_description"]),
        "crop_moisture":str(crop["crop_moisture"]),
        "crop_temp":str(crop["crop_temp"]),
        "crop_status":str(crop["crop_status"]),
        "crop_created_at":str(crop["crop_created_at"]),
        "crop_updated_at":str(crop["crop_updated_at"]),
        
    }

def crop_list_serial(crops) -> list:
    return [crop_serial(crop) for crop in crops]

#crop_log db schema
def crop_log_serial(crop_log) -> dict:
    return{
        "crop_date_planted":str(crop_log["crop_date_planted"]),
        "crop_date_harvested":str(crop_log["crop_date_harvested"]),
        "crop_id":str(crop_log["crop_id"])
    }

def crop_log_list_serial(crop_logs) -> list:
    return [crop_log_serial(crop_log) for crop_log in crop_logs]

#notification db schema
def notification_list_serial(notification) -> dict:
    return{
        "user_id":str(notification["user_id"]),
        "crop_id":str(notification["crop_id"])
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