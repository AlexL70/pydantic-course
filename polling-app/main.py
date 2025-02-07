from fastapi import FastAPI
from pydantic import ValidationError
from app.models.Polls import Poll
from typing import List

app = FastAPI()

@app.get("/test")
def test():
    return {"message": "Hello there!"}

@app.post("/polls/create")
def create_poll(poll: Poll) -> Poll:
    return poll