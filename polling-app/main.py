from fastapi import FastAPI
from app.api.polls import router as polls_router

app = FastAPI()
app.include_router(polls_router, prefix="/polls", tags=["Polls CRUD"])

@app.get("/test")
def test():
    return {"message": "Hello there!"}
