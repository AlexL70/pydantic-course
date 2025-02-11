from fastapi import FastAPI
from app.api.polls import router as polls_router

app = FastAPI(
    title="Polls API",
    description="A simple API to create and vote on polls.",
    version="0.1",
    openapi_tags=[
        {
            "name": "Polls",
            "description": "Operations related to creating and viewing polls." 
        }
    ]
)

app.include_router(polls_router, prefix="/polls", tags=["Polls"])