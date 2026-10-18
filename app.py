from fastapi import FastAPI
 
app = FastAPI()
 
@app.get("/")
def home():
    return {"message": "Hello from Python on Vercel"}

@app.get("/data")
def data():
    return {"message":12.25}
