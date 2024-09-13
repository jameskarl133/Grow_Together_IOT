def farmer_serial(farmer) -> dict:
    return{
        "id":str(farmer["_id"]),
        "fname":str(farmer["fname"]),
        "mname":str(farmer["mname"]),
        "lname":str(farmer["lname"]),
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
