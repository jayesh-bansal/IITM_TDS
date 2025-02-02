from fastapi import FastAPI, Query
from mangum import Mangum
import json
import os

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
# Load marks from JSON file
current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, 'q-vercel-python.json')

with open(json_path) as f:
    MARK_DB = json.load(f)

@app.get("/api")
async def get_marks(names: list[str] = Query(...)):
    try:
        return {"marks": [MARK_DB.get(name) for name in names]}
    except Exception as e:
        raise HTTPException(500, detail=str(e))

handler = Mangum(app)
