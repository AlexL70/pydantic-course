from pydantic import BaseModel, Field, field_validator
from uuid import UUID, uuid4
from typing import List, Optional
from datetime import datetime, timezone
from app.models.Choice import Choice

class PollCreate(BaseModel):
    """Poll creating data model"""
    title: str = Field(min_length=5, max_length=50)
    options: List[str]
    expires_at: Optional[datetime] = None

    @field_validator("options", mode="after")
    @classmethod
    def validate_options(cls, v: List[str]) -> List[str]:
        if len(v) < 2 or len(v) > 5:
            raise ValueError("A poll must contain from 2 to 5 options.")
        return v

    def create_poll(self) -> "Poll":
        """Create a new poll instance with auto-incrementing labels for choices""" 
        choices = [Choice(description=o, label=index+1) for index, o in
            enumerate(self.option)
        ]
        if self.expires_at is not None and self.expires_at <= datetime.now(timezone.utc):
            raise ValueError("Expiration date must be in the future.")

        return Poll(options=choices, title=self.title, expires_at=self.expires_at)

class Poll(PollCreate):
    """Poll data model"""
    id: UUID = Field(default_factory=uuid4)
    options: List[Choice]
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )