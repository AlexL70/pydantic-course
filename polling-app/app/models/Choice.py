from pydantic import BaseModel, Field
from uuid import UUID, uuid4

class ChoiceCreate(BaseModel):
    """Model for creating a new choice"""
    description: str = Field(min_length=1, max_length=100)

class Choice(ChoiceCreate):
    """Model representing a single choice in a poll"""
    id: UUID = Field(default_factory=uuid4)
    label: int = Field(ge=1, le=5)