from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import List, Optional
from datetime import datetime, timezone
from Choice import Choice

class PollCreate(BaseModel):
    """Poll creating data model"""
    title: str = Field(min_length=5, max_length=50)
    options: List[str]
    expires_at: Optional[datetime] = None

class Poll(PollCreate):
    """Poll data model"""
    id: UUID = Field(default_factory=uuid4)
    options: List[Choice]
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )