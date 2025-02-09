from app.models.Polls import Poll
from redis import Redis
from dotenv import load_dotenv
from uuid import UUID
from typing import Optional
import os

load_dotenv()

redis_client = Redis(
    host = os.getenv("REDIS_HOST"),
    port = os.getenv("REDIS_PORT"),
    password = os.getenv("REDIS_PASSWORD"),
    db = os.getenv("REDIS_DB")
)
redis_client.ping()


def save_poll(poll: Poll) -> None:
    poll_json = poll.model_dump_json()
    redis_client.set(f"poll:{poll.id}", poll_json)

def retrieve_poll(poll_id: UUID) -> Optional[Poll]:
    poll_json = redis_client.get(f"poll:{poll_id}")
    if poll_json:
        poll = Poll.model_validate_json(poll_json)
        return poll
    return None