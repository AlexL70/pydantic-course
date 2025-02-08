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