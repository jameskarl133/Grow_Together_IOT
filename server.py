from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")

try:
    client = MongoClient(config["URI"])
    db = client["Grow_Together"]
    print('MongoDB Database connected')


except:
    print('MongoDB not connected')
    exit()

farmer = db['farmer']
