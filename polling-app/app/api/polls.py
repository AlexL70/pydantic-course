from fastapi import FastAPI, status, Response, HTTPException, APIRouter
from pydantic import ValidationError
from typing import Optional
from uuid import UUID
from app.models.Polls import PollCreate, Poll
from app.services import utils


router = APIRouter()

@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_poll(poll: PollCreate, response: Response) -> Poll:
    try:
        created = poll.create_poll()
        utils.save_poll(created)
        return created
    except ValidationError as e:
        return e

@router.get("/get/{id}", status_code=status.HTTP_200_OK)
def get_poll(id: UUID, response: Response) -> Optional[Poll]:
    try:
        poll = utils.retrieve_poll(id)
        if not poll:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Poll with id='{id}' is not found.")
        return poll
    except ValidationError as e:
        return e
