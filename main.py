from fastapi import FastAPI, Query
from mangum import Mangum
import json
import os

app = FastAPI()

# Load marks from JSON file
current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, 'q-vercel-python.json')

with open(json_path) as f:
    MARK_DB = json.load(f)

@app.get("/api")
async def get_marks(names: list[str] = Query(...)):
    return {
        "marks": [MARK_DB.get(name, None) for name in names]
    }

handler = Mangum(app)
