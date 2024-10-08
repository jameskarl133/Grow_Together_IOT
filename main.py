from fastapi import FastAPI
from routes import router

# FastAPI app instance
app = FastAPI()

# Include the routes
app.include_router(router)

# Hello World endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}
