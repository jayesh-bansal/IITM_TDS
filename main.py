from fastapi import FastAPI, Query
from mangum import Mangum
import json
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
