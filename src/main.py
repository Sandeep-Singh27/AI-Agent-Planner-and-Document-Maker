from fastapi import FastAPI
from src.schema import UserRequest

app = FastAPI()

@app.post("/agent")
def handle_request(request:UserRequest):
    