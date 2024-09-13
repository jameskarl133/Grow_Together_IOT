# all the imports
from fastapi import FastAPI
from routes import router

# creating a server with python FastAPI
app = FastAPI()
app.include_router(router)

# hello world endpoint
@app.get("/")
def read_root(): # function that is binded with the endpoint
    return {"Hello": "World"}
