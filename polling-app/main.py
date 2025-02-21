from fastapi import FastAPI
from app.api.polls import router as polls_router
from app.api.votes import router as votes_router

app = FastAPI(
    title="Polls API",
    description="A simple API to create and vote on polls.",
    version="0.1",
    openapi_tags=[
        {
            "name": "Polls",
            "description": "Operations related to creating and viewing polls." 
        },
        {
            "name": "Votes",
            "description": "Operations related to casting votes."
        }
    ]
)

app.include_router(polls_router, prefix="/polls", tags=["Polls"])
app.include_router(votes_router, prefix="/votes", tags=["Votes"])