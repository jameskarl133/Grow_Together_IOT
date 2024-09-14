def farmer_serial(farmer) -> dict:
    return{
        "id":str(farmer["_id"]),
        "fname":str(farmer["fname"]),
        "mname":str(farmer["mname"]),
        "lname":str(farmer["lname"]),
        "field_type":str(farmer["field_type"]),
        "dob":str(farmer["dob"]),
        "email":str(farmer["email"]),
        "address":str(farmer["address"]),
        "phno":str(farmer["phno"]),
        "username":str(farmer["username"]),
        "password":str(farmer["password"]),
        "status":str(farmer["status"]),
        "created_at":str(farmer["created_at"]),
        "updated_at":str(farmer["updated_at"]),
        "img":str(farmer["img"]),
        
    }

def farmer_list_serial(farmers) -> list:
    return [farmer_serial(farmer) for farmer in farmers]


def crop_serial(crop) -> dict:
    return{
        "id":str(crop["_id"]),
        "crop_name":str(crop["name"]),
        "crop_image":str(crop["image"]),
        "crop_soil":str(crop["crop_soil"]),
        "crop_moisture":str(crop["crop_moisture"]),
        "crop_temp":str(crop["crop_temp"]),
        "crop_status":str(crop["crop_status"]),
        "crop_created_at":str(crop["crop_created_at"]),
        "crop_updated_at":str(crop["crop_updated_at"]),
        
    }

def crop_list_serial(crops) -> list:
    return [crop_serial(crop) for crop in crops]
