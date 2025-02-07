from fastapi import FastAPI
from pydantic import ValidationError
from app.models.Polls import Poll, PollCreate

app = FastAPI()

@app.get("/test")
def test():
    return {"message": "Hello there!"}

@app.post("/polls/create")
def create_poll(poll: PollCreate) -> Poll:
    return Poll(title=poll.title,
                options=["first", "second"])