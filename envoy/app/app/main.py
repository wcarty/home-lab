# app/main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI behind Envoy!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
