from fastapi import FastAPI
from pydantic import ValidationError
from app.models.Polls import Poll, PollCreate

app = FastAPI()

@app.get("/test")
def test():
    return {"message": "Hello there!"}

@app.post("/polls/create")
def create_poll(poll: PollCreate):
    try:
        created = poll.create_poll()
        return {
            "detail": "Poll successfully created",
            "poll_id": created.id
        }
    except ValidationError as e:
        return e