from fastapi import FastAPI, status
from pydantic import ValidationError
from app.models.Polls import PollCreate

app = FastAPI()

@app.get("/test")
def test():
    return {"message": "Hello there!"}

@app.post("/polls/create", status_code=status.HTTP_201_CREATED)
def create_poll(poll: PollCreate):
    try:
        created = poll.create_poll()
        return {
            "detail": "Poll successfully created",
            "poll_id": created.id,
            "poll": created
        }
    except ValidationError as e:
        return e

        
### explore and throw away ###
from redis import Redis
from dotenv import load_dotenv
import os

load_dotenv()

redis_client = Redis(
    host = os.getenv("REDIS_HOST"),
    port = os.getenv("REDIS_PORT"),
    password = os.getenv("REDIS_PASSWORD"),
    db = os.getenv("REDIS_DB")
)
redis_client.ping()

@app.post("/redis/save")
def save_redis(id: str, name: str):
    redis_client.set(id, name)
    return {"status": "success"}

@app.get("/redis/get/{id}")
def retrieve_redis(id: str):
    result = redis_client.get(id)
    return {"result": result}