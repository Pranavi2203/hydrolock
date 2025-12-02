from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/hello")
def hello():
    return {"message": "Hello from HydroLock platform!"}

@app.get("/hello1")
def hello():
    return {"message": "Hello from HydroLock platform v2!"}