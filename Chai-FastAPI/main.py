from fastapi import FastAPI
from pydentic import BaseModel
from typing import List

app = FastAPI()

@app.get("/")
def show():
    return {"message":"This is home page"}