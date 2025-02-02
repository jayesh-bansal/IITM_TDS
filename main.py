from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
def read_root():
    return {"message": "Hello, World!"}

@app.get("?name={marks1}&?name={marks2}")
def marks():
    return {"marks": [marks1, marks2] )
