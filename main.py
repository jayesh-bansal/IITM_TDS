from fastapi import FastAPI

app = FastAPI()

@app.get("/api?name={marks1}&name={marks2}")
def marks():
    return {"marks": [marks1, marks2] )
