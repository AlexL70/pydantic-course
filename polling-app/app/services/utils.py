from app.models.Polls import Poll
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

def save_poll(poll: Poll):
    poll_json = poll.model_dump_json()
    redis_client.set(f"poll:{poll.id}", poll_json)