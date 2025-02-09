from fastapi import FastAPI, status
from pydantic import ValidationError
from app.models.Polls import PollCreate, Poll
from app.services import utils

app = FastAPI()

@app.get("/test")
def test():
    return {"message": "Hello there!"}

@app.post("/polls/create", status_code=status.HTTP_201_CREATED)
def create_poll(poll: PollCreate) -> Poll:
    try:
        created = poll.create_poll()
        utils.save_poll(created)
        return created
    except ValidationError as e:
        return e
